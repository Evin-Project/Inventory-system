# Generated by Django 3.0.7 on 2023-10-25 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20231025_1043'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TransferIn',
        ),
    ]