from django.db import models
# Model field reference: https://docs.djangoproject.com/en/3.1/ref/models/fields/

# NOTE: A model class represents a database table, and an instance of that class
# represents a particular record in the database table.

# Create your models (classes) here.
class Project (models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title