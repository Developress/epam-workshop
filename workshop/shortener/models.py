from django.db import models


# Create your models here.
class Shortened(models.Model):
    initial_url = models.CharField(max_length=1000)
    shortened = models.CharField(max_length=10, unique=True)