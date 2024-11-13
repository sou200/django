from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    authour = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13)
    def __str__(self):
        return self.title
    
