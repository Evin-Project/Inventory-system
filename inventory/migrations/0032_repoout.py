# Generated by Django 4.2.6 on 2023-11-09 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0031_customer_inventory_repoin'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepoOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
            ],
        ),
    ]