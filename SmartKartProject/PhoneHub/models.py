from django.db import models

# Create your models here.
class PhoneModel(models.Model):
    brand = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media", null=True, blank=True)
    name = models.CharField(max_length=50)
    camera = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    price = models.FloatField()