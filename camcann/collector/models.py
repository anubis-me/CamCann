from django.db import models
import datetime
class x(models.Model):
    camera = models.CharField(max_length=150)
    Gender = models.CharField(max_length=20)
    Age = models.IntegerField(max_length=5)