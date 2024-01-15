from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pic')
    desc=models.TextField()
class place2(models.Model):
    date=models.TextField()
    month=models.TextField()
    image=models.ImageField(upload_to='pic')
    subscript=models.TextField()
    desc=models.TextField()
