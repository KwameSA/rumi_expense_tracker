import pandas as pd
from django.core.management.base import BaseCommand

from books.models import Book, BookCategory


class Command(BaseCommand):
    help = "Import books distribution expenses from Excel spreadsheet"

    def handle(self, *args, **kwargs):
        df = pd.read_excel("data/books_distribution_expenses.xlsx")

        print("Long authors:")
        print(df[df['authors'].str.len() > 200])

        print("Long publishers:")
        print(df[df['publisher'].str.len() > 200])

        # Fill missing categories with "Uncategorized"
        df["category"] = df["category"].fillna("Uncategorized")
        # Fill missing subtitles with empty string
        df["subtitle"] = df["subtitle"].fillna("")

        for i, row in df.iterrows():
            category, _ = BookCategory.objects.get_or_create(name=row["category"])

            Book.objects.create(
                title=row["title"],
                subtitle=row["subtitle"].strip(),
                authors=row["authors"],
                publisher=row["publisher"],
                published_date=pd.to_datetime(row["published_date"]).date(),
                category=category,
                distribution_expense=row["distribution_expense"],
            )

        self.stdout.write(self.style.SUCCESS("Books Imported Successfully!"))
