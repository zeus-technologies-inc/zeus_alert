# Generated by Django 2.0.9 on 2018-11-14 13:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20181114_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='ORG_members',
            field=models.ManyToManyField(blank=True, null=True, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
