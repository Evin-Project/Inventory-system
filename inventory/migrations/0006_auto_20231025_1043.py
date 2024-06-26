# Generated by Django 3.0.7 on 2023-10-25 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20231025_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransferIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Date')),
                ('control_number', models.IntegerField(blank=True, null=True, verbose_name='Control Number')),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Branch')),
                ('motor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Motor')),
            ],
        ),
        migrations.DeleteModel(
            name='TransferOut',
        ),
    ]
