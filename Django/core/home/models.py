from django.db import models

# Create your models here.

class student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    # image = models.ImageField()
    file = models.FileField()
    birth_date = models.DateField()
    cgpa = models.DecimalField(max_digits=10,decimal_places=2)