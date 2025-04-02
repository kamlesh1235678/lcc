from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=10)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)