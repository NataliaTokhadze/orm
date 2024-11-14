from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    pages = models.IntegerField()
    title = models.CharField(max_length=255)
    descriprion = models.TextField()
    price = models.IntegerField()
    
    def __str__(self):
        return f'{self.title} written by {self.author}'
