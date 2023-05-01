# Generated by Django 4.1.6 on 2023-05-01 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contractor', '0020_requestservice_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestservice',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for Service', 'Out for Service'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
    ]
