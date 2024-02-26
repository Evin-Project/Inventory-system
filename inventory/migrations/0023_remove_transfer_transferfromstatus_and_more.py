# Generated by Django 4.2.6 on 2023-11-04 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0022_transfer_remove_transferout_inventory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='transferfromstatus',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='transfertostatus',
        ),
        migrations.AddField(
            model_name='transfer',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transfers_from_status', to='inventory.status'),
        ),
    ]