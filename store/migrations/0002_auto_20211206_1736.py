# Generated by Django 3.2.9 on 2021-12-06 12:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customers',
            new_name='Customer',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
