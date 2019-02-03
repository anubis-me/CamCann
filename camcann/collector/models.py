from django.db import models
import datetime
import os

def get_image_path(instance, filename):
    return os.path.join('images', str(instance.id), filename)

class x(models.Model):
    camera = models.CharField(max_length=150)
    Gender = models.CharField(max_length=20)
    Age = models.IntegerField()
    Image = models.ImageField(upload_to = get_image_path)
    Timestamp = models.DateTimeField()
    yaw = models.IntegerField()
    pitch = models.IntegerField()
    roll = models.IntegerField()