from django.db import models

# Create your models here.
class Book(models.Model):
    # to structure the type of data we wish to store
    # all fields are short text hence the use of charfield
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)