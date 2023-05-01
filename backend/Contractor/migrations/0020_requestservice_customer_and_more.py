# Generated by Django 4.1.6 on 2023-05-01 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Contractor', '0019_requestservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestservice',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='requestservice',
            name='contractor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contractor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='requestservice',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contractor.service'),
        ),
    ]
