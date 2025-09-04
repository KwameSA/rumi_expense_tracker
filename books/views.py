from django.core.paginator import Paginator
from django.db.models import Sum
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .forms import BookCategoryForm, BookForm
from .models import Book, BookCategory
from django.http import JsonResponse
from django.db.models.functions import ExtractYear


def book_list(request):
    books = Book.objects.all().order_by("id")
    paginator = Paginator(books, 20) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "books/book_list.html", {"page_obj": page_obj})


# Category Views
class CategoryListView(ListView):
    model = BookCategory
    template_name = "books/category_list.html"
    context_object_name = "categories"


class CategoryCreateView(CreateView):
    model = BookCategory
    form_class = BookCategoryForm
    template_name = "books/category_form.html"
    success_url = reverse_lazy("category_list")


class CategoryUpdateView(UpdateView):
    model = BookCategory
    form_class = BookCategoryForm
    template_name = "books/category_form.html"
    success_url = reverse_lazy("category_list")


class CategoryDeleteView(DeleteView):
    model = BookCategory
    template_name = "books/category_confirm_delete.html"
    success_url = reverse_lazy("category_list")


# Book Views
class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"
    paginate_by = 20

    def get_queryset(self):
        queryset = Book.objects.all().order_by("id")
        q = self.request.GET.get("q")
        year = self.request.GET.get("year")

        if q:
            q_upper = q.upper().strip()
            query = Q(title__icontains=q) | Q(authors__icontains=q) | Q(subtitle__icontains=q) | Q(publisher__icontains=q) | Q(category__name__icontains=q)

            # If user typed a display_id like "B0338", match the numeric id
            if q_upper.startswith("B") and q_upper[1:].isdigit():
                query |= Q(id=int(q_upper[1:]))
            # Optional: match just a number like "338" as well
            elif q.isdigit():
                query |= Q(id=int(q))

            queryset = queryset.filter(query)

        if year and year.isdigit():
            queryset = queryset.filter(published_date__year=int(year))

        return queryset



class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_form.html"
    success_url = reverse_lazy("book_list")


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_form.html"
    success_url = reverse_lazy("book_list")


class BookDeleteView(DeleteView):
    model = Book
    template_name = "books/book_confirm_delete.html"
    success_url = reverse_lazy("book_list")

def reports(request):
    return render(request, "books/reports.html")

def get_chart_data(request):
    report_type = request.GET.get('report', 'expense')

    if report_type == 'expense':
        categories = BookCategory.objects.all()
        labels = [c.name for c in categories]
        data = [
            sum(
                b.distribution_expense
                for b in Book.objects.filter(category=c)
            )
            for c in categories
        ]
        chart_type = 'pie'

    elif report_type == 'books_year':
        years = Book.objects.dates('published_date', 'year')
        labels = [str(y.year) for y in years]
        data = [
            Book.objects.filter(published_date__year=y.year).count()
            for y in years
        ]
        chart_type = 'bar'

    elif report_type == 'books_category':
        categories = BookCategory.objects.all()
        labels = [str(c.name) for c in categories]
        data = [
            Book.objects.filter(category=c).count()
            for c in categories
        ]
        chart_type = 'bar'

    elif report_type == 'books_publisher':
        qs = Book.objects.values('publisher').annotate(count=Count('id')).order_by('publisher')
        labels = [str(b['publisher']) for b in qs]
        data = [b['count'] for b in qs]
        chart_type = 'bar'

    elif report_type == 'best_authors':
        qs = (
            Book.objects
            .values('authors')
            .annotate(count=Count('authors'))
            .order_by('-count')[:10]
        )
        labels = [b['authors'] for b in qs]
        data = [b['count'] for b in qs]
        chart_type = 'bar'

    elif report_type == 'books_trend':
        qs = Book.objects.annotate(year=ExtractYear('published_date'))\
            .values('year')\
            .annotate(count=Count('id'))\
            .order_by('year')

        labels = [b['year'] for b in qs]
        data = [b['count'] for b in qs]
        chart_type = 'line'

    elif report_type == 'top_expense_titles':
        qs = Book.objects.order_by('-distribution_expense')[:10]
        labels = [b.title for b in qs]
        return JsonResponse({
            'labels': labels,
            'data': [],          
            'chart_type': 'list'
        })

    else:
        labels, data, chart_type = [], [], 'bar'

    return JsonResponse({
        'labels': labels,
        'data': data,
        'chart_type': chart_type
    })