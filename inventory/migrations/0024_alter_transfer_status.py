# Generated by Django 4.2.6 on 2023-11-04 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0023_remove_transfer_transferfromstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.status'),
        ),
    ]