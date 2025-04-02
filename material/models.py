from django.db import models

# Create your models here.

class Matrial(models.Model):
    type = models.CharField(max_length=250)
    name = models.CharField(max_length=999)
    brand = models.CharField(max_length=250)
    start_rate = models.FloatField()
    end_rate  = models.FloatField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to="matrial_image" , null= True , blank=True)


class MatrialReview(models.Model):
    matrial = models.ForeignKey(Matrial , on_delete=models.CASCADE , related_name="matrial_review")
    user_name = models.CharField(max_length=250)
    contact_number = models.CharField(max_length=10)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)