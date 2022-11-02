# Generated by Django 3.1.4 on 2022-10-30 19:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Firstname',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='Lastname',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
