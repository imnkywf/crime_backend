# Generated by Django 3.2.24 on 2024-02-08 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20240208_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
