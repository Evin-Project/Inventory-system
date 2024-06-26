# Generated by Django 4.2.6 on 2023-11-13 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0034_remove_releaseout_inventory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='releaseout',
            name='customer_history',
        ),
        migrations.AddField(
            model_name='releaseout',
            name='comaker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.comaker'),
        ),
        migrations.AddField(
            model_name='releaseout',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.customer'),
        ),
        migrations.AddField(
            model_name='releaseout',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.payment'),
        ),
        migrations.AddField(
            model_name='releaseout',
            name='salestype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.salestype'),
        ),
    ]
