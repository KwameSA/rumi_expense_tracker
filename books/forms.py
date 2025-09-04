from django import forms

from .models import Book, BookCategory


class BookCategoryForm(forms.ModelForm):
    class Meta:
        model = BookCategory
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter Category Name"}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "subtitle",
            "authors",
            "publisher",
            "published_date",
            "category",
            "distribution_expense",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter Book Title"}),
            "subtitle": forms.TextInput(attrs={"placeholder": "Enter Book Subitle"}),
            "authors": forms.TextInput(
                attrs={"placeholder": "Enter Author(s) Name(s)"}
            ),
            "publisher": forms.TextInput(attrs={"placeholder": "Enter Publisher Name"}),
            "published_date": forms.DateInput(attrs={"type": "date"}),
            "distribution_expense": forms.NumberInput(
                attrs={"placeholder": "Enter Expense"}
            ),
        }
