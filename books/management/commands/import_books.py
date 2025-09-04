import pandas as pd
from django.core.management.base import BaseCommand

from books.models import Book, BookCategory


class Command(BaseCommand):
    help = "Import books distribution expenses from Excel spreadsheet"

    def handle(self, *args, **kwargs):
        df = pd.read_excel("data/books_distribution_expenses.xlsx")

        for i, row in df.iterrows():
            category, created = BookCategory.objects.get_or_create(name=row["category"])

            Book.objects.create(
                title=row["title"],
                subtitle=row["subtitle"],
                authors=row["authors"],
                publisher=row["publisher"],
                published_date=pd.to_datetime(row["published_date"]).date(),
                category=category,
                distribution_expense=row["distribution_expense"],
            )

        self.stdout.write(self.style.SUCCESS("Books Imported Successfully!"))
