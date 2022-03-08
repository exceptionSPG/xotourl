from django.db import models

# Create your models here.
#Admin@123

class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)

