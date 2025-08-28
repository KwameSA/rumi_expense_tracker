from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Sum
from .models import Book, BookCategory
from .forms import BookForm, BookCategoryForm

# Category Views
class CategoryListView(ListView):
    model = BookCategory
    template_name = 'books/category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = BookCategory
    form_class = BookCategoryForm
    template_name = 'books/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = BookCategory
    form_class = BookCategoryForm
    template_name = 'books/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = BookCategory
    template_name = 'books/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

# Book Views
class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete'
    success_url = reverse_lazy('book_list')


def expense_report(request):
    categories = BookCategory.objects.all()
    labels = [cat.name for cat in categories]
    data = [float(Book.objects.filter(category=cat).aggregate(Sum('distribution_expense'))['distribution_expense__sum'] or 0) for cat in categories]
    return render(request, 'books/report.html', {'labels': labels, 'data':data})