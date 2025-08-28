from django import forms
from .models import Book, BookCategory

class BookCategoryForm(forms.ModelForm):
    class Meta:
        model = BookCategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Category Name'}),
        }

    class BookForm(forms.ModelForm):
        class Meta:
            model = Book
            fields = ['id_number', 'title', 'author', 'category', 'publish_date', 'distribution_expense']
            widgets = {
                'title': forms.TextInput(attrs={'placeholder': 'Enter Book Title'}),
                'author': forms.TextInput(attrs={'placeholder': 'Enter Author Name'}),
                'publish_date': forms.DateInput(attrs={'type': 'date'}),
                'distribution_expense': forms.NumberInput(attrs={'placeholder': 'Enter Expense'})
            }