# Generated by Django 4.2.6 on 2023-11-14 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0039_remove_customer_inventory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='comaker',
        ),
        migrations.AddField(
            model_name='customer_history',
            name='comaker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.comaker'),
        ),
    ]
