# Generated by Django 4.0.6 on 2022-08-09 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='video',
            field=models.CharField(max_length=500),
        ),
    ]
