from django.db import models

class BookCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Book(models.Model):
        id_number =  models.CharField(max_length=200)
        title = models.CharField(max_length=200)
        author = models.CharField(max_length=100)
        publish_date = models.DateField()
        category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
        distribution_expense = models.DecimalField(max_digits=10, decimal_places=2)

        class Meta:
            ordering = ['title']

        def __str__(self):
            return f"{self.title} by {self.author}"