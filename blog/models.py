

from statistics import mode
from tabnanny import verbose
from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=1000, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

class BlogModel(models.Model):
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="posts", on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=1000)
    intro = models.TextField()
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='blog')
    create_at = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-create_at',)

class Comments(models.Model):
    post = models.ForeignKey(BlogModel, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True) 