# Generated by Django 2.1.5 on 2019-02-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0004_auto_20190202_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='image_name',
            field=models.CharField(default='images1', max_length=150),
        ),
    ]
