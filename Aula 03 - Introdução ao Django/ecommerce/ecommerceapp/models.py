from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    director = models.ForeignKey(Director, null=True, on_delete=models.CASCADE)
    poster_url = models.URLField()

    def __str__(self):
        return self.title
