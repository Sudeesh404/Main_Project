from django.db import models
from myapp.models import *

# Create your models here.

class Admin(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    user_id = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    pic = models.FileField(upload_to = 'Profile', default='default.jpg')

    def __str__(self):
        return self.fname + " " + self.lname
        
class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('myapp.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
