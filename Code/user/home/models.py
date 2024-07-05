from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=18)
    mail=models.CharField(max_length=18)
    age=models.CharField(max_length=18)
    desc=models.TextField()