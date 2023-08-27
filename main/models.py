from django.db import models
import datetime


class Book_Table(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    date = models.DateField(null=False, default=datetime.date.today)
    person = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name
