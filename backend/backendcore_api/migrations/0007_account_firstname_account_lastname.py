# Generated by Django 4.1.6 on 2023-02-28 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendcore_api', '0006_account_contractor_contractor_zipcode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='firstname',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='lastname',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
