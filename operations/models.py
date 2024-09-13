from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()


    def __str__(self):
        return self.name

