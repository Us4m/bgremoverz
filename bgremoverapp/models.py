from django.db import models

# Create your models here.  
class Image(models.Model):
    name = models.CharField(max_length=255)
    original_image = models.ImageField(upload_to='original/')
    masked_image = models.ImageField(upload_to='masked/')
