from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    TABLES = (
        ('T', 'To do'),
        ('I', 'In progress'),
        ('D', 'Done'),
    )
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.CharField(max_length=1, choices=TABLES)
    def __str__(self):
        return self.text
