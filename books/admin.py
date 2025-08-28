from django.contrib import admin

from .models import Book, BookCategory

@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'title', 'author', 'category', 'publish_date', 'distribution_expense')
    list_filter = ('category', 'publish_date')
    search_fields = ('title', 'author')