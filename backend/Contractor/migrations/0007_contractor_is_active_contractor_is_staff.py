# Generated by Django 4.1.6 on 2023-03-11 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contractor', '0006_alter_contractor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contractor',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]