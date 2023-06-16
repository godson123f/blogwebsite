from django.db import models


class blog(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='picture', null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)
    cate = models.CharField(max_length=50)
    desc = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return '{}'.format(self.name)


class add(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='picture')
    cate = models.CharField(max_length=50)
    date = models.DateField()
