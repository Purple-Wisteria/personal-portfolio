from django.contrib import admin

# Read More about Django admin site: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site
# Specifying the models that we want to show up in the admin.
from .models import Project

admin.site.register(Project)