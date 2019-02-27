from django.db import models


class Data(models.Model):
    image_name = models.CharField(max_length=150, default="")
    head_roll = models.CharField(max_length=150, default="")
    head_yaw = models.CharField(max_length=150, default="")
    camera = models.CharField(max_length=150, default="")
    head_pitch = models.CharField(max_length=150, default="")
    Frame_Shape = models.CharField(max_length=150, default= [0,0,0])
    Age = models.IntegerField(default="NA")
    Image = models.CharField(max_length=150, default="images1")
    Gender = models.CharField(max_length=20, default="NA")
    Location = models.CharField(max_length=300, default="images/")
    Timestamp = models.CharField(max_length=250, default="000000")

    def __str__(self):
        return self.Image + '-' + self.Gender + '-' + str(self.Age)
