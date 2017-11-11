from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    def slug(self):
        return slugify(self.abbreviation)

    def get_absolute_url(self):
        return reverse('state_index', kwargs = {'state_abrv': self.slug()})
