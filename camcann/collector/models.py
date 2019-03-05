from django.db import models
import json

class Data(models.Model):
    image_name = models.CharField(max_length=150,blank=True,default=None,null=True)
    camera = models.CharField(max_length=150,blank=True,default=None,null=True)
    Frame_Shape = models.CharField(max_length=150)
    Age = models.IntegerField()
    Image = models.TextField(blank=True,default=None,null=True)
    Gender = models.CharField(max_length=20)
    Location = models.CharField(max_length=300,blank=True,default=None,null=True)
    Timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Gender + '-' + str(self.Age)

class Ads(models.Model):
    target_age_start = models.IntegerField()
    target_age_end = models.IntegerField()
    campaign_name = models.CharField(max_length=127,default='-')
    target_gender = models.CharField(max_length=127)
    video_file = models.CharField(max_length=1024)

    def __str__(self):
        return self.campaign_name

class Queue(models.Model):
    ad = models.ForeignKey(Ads,on_delete=models.CASCADE)
    played = models.BooleanField(default=False)

class Tag(models.Model):
    name = models.CharField(max_length=128)
    tag_id = models.CharField(max_length=128)
    image = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

class TagHistory(models.Model):
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=128)

class AdTarget(models.Model):
    ad = models.ForeignKey(Ads,on_delete=models.CASCADE)
    person = models.ForeignKey(Data,on_delete=models.CASCADE)
    count = models.IntegerField(default=0)