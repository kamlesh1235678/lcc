from django.db import models

# Create your models here.
class Labour(models.Model):
    name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=10)
    expert_title = models.CharField(max_length=250)
    desc = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=999 , null = True , blank=  True)
    image = models.FileField(upload_to="labour_image/", null = True , blank=  True)


class LabourReview(models.Model):
    labour = models.ForeignKey(Labour , on_delete=models.CASCADE , related_name="labour_review")
    user_name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=10)
    desc = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)