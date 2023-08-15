from django.db import models

# Create your models here.

class Discount(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)
    percentage = models.IntegerField(blank=True, default=0)
    cover_image = models.URLField(blank=True) 
    