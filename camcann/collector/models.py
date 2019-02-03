from django.db import models


class Data(models.Model):
    camera = models.CharField(max_length=150)
    Gender = models.CharField(max_length=20)
    Age = models.IntegerField(max_length=5)
    image_name = models.CharField(max_length=150,default="images1")
    Image = "/images/" + str(image_name)

    def __str__(self):
        return self.camera + '-' + self.Gender + '-' + str(self.Age)

