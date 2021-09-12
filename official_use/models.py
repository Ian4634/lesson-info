from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    discription = models.TextField(max_length=2000, blank=True)
    image = models.ImageField(blank=True, null = True, upload_to= 'images/categoryimage/')

class Lesson(models.Model):
    name = models.CharField(max_length=200, blank=True)
    category = models.ManyToManyField(Category,blank=True, null=True)
    location = models.CharField(max_length=500, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    eligibility = models.CharField(max_length=500, blank=True)
    link = models.URLField(max_length=500)
    discription = models.TextField(max_length=2000, blank=True)
    image = models.ImageField(blank=True, null = True, upload_to= 'images/lessonimage/')

