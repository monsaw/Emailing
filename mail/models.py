from django.db import models
from django.urls.base import reverse

# Create your models here.

class Email(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('mail:emails')