# Generated by Django 2.1.5 on 2019-02-01 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='x',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camera', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('Age', models.IntegerField(max_length=5)),
            ],
        ),
    ]
