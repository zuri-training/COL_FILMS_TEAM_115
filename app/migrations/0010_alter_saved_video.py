# Generated by Django 4.0.6 on 2022-08-14 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0003_upload_no_of_reacts'),
        ('app', '0009_rename_save_saved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saved',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploads.upload'),
        ),
    ]
