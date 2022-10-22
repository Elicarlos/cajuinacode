from distutils.errors import CompileError
from django.contrib import admin

from blog.models import BlogModel
from blog.models import Comments
from blog.models import Category

# Register your models here.
admin.site.register(BlogModel)
admin.site.register(Comments)
admin.site.register(Category)