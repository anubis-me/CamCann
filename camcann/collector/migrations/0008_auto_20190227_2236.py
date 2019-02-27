# Generated by Django 2.1.5 on 2019-02-27 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0007_auto_20190227_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='camera',
            field=models.CharField(default='NA', max_length=150),
        ),
        migrations.AlterField(
            model_name='data',
            name='head_pitch',
            field=models.CharField(default='NA', max_length=150),
        ),
        migrations.AlterField(
            model_name='data',
            name='head_roll',
            field=models.CharField(default='NA', max_length=150),
        ),
        migrations.AlterField(
            model_name='data',
            name='head_yaw',
            field=models.CharField(default='NA', max_length=150),
        ),
        migrations.AlterField(
            model_name='data',
            name='image_name',
            field=models.CharField(default='NA', max_length=150),
        ),
    ]