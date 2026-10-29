from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Expenses(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return self.title
