# Generated by Django 4.1.6 on 2023-04-12 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendcore_api', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
