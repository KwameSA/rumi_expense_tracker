from django.contrib import admin
from .models import Book, BookCategory


@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "subtitle",
        "authors",
        "publisher",
        "published_date",
        "category",
        "distribution_expense",
    )
    list_filter = ("category", "published_date")
    search_fields = ("title", "authors")
