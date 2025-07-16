from django.db import models

# Create your models here.
class Idea(models.Model):
    title = models.CharField(max_length=32)
    photo = models.ImageField('이미지', blank=True, upload_to='ideas/%Y%m%d')
    content = models.TextField()
    interest = models.CharField(max_length=32)
    devtool = models.CharField(max_length=32)