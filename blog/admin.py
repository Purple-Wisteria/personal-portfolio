from django.contrib import admin

# Register your models here.
# Read More about Django admin site: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site
# Specifying the models that we want to show up in the admin.
from .models import Blog
admin.site.register(Blog)