from django.db import models


class blog(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='picture')
    cate = models.CharField(max_length=50)
    desc = models.TextField()
    author = models.CharField(max_length=50)
    date=models.DateField()
class add(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='picture')
    cate = models.CharField(max_length=50)
    date=models.DateField()










































































