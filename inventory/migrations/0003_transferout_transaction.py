# Generated by Django 3.0.7 on 2023-10-25 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20231025_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='transferout',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Transaction'),
        ),
    ]