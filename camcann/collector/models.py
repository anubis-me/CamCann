from django.db import models


class Data(models.Model):
    camera = models.CharField(max_length=150)
    Gender = models.CharField(max_length=20)
    Age = models.IntegerField(max_length=5)
    image_name = models.CharField(max_length=150, default="images1")
    Image = "/images/" + str(image_name)
    head_yaw = models.FloatField(max_length=200, default=0)
    head_pitch = models.FloatField(max_length=200, default=0)
    head_roll = models.FloatField(max_length=200, default=0)
    Timestamp = models.CharField(max_length=250, default="000000")

    def __str__(self):
        return self.camera + '-' + self.Gender + '-' + str(self.Age)
