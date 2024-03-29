# Generated by Django 4.1.6 on 2023-05-01 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Contractor', '0018_remove_service_user_service_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_request', models.DateTimeField(auto_now_add=True)),
                ('contractor', models.ForeignKey(limit_choices_to={'groups__name': 'Contractor'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(limit_choices_to=models.Q(('account__in', models.F('contractor__account_set'))), on_delete=django.db.models.deletion.CASCADE, to='Contractor.service')),
            ],
        ),
    ]
