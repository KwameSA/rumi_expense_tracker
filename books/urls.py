from django.urls import path

from . import views

urlpatterns = [
    # Home -> redirect to books list
    path("", views.BookListView.as_view(), name="home"),
    # Category URLs
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path("categories/add/", views.CategoryCreateView.as_view(), name="category_add"),
    path(
        "categories/<int:pk>/edit/",
        views.CategoryUpdateView.as_view(),
        name="category_edit",
    ),
    path(
        "categories/<int:pk>/delete/",
        views.CategoryDeleteView.as_view(),
        name="category_delete",
    ),
    # Book URLs
    path("books/", views.BookListView.as_view(), name="book_list"),
    path("books/add/", views.BookCreateView.as_view(), name="book_add"),
    path("books/<int:pk>/edit/", views.BookUpdateView.as_view(), name="book_edit"),
    path("books/<int:pk>/delete/", views.BookDeleteView.as_view(), name="book_delete"),
    path("reports/", views.reports, name="reports"),
    path("reports/data/", views.get_chart_data, name='get_chart_data')
]
