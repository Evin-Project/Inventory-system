# Generated by Django 3.0.7 on 2023-10-27 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_transferout'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransferIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('controlnumber', models.IntegerField(blank=True, null=True, verbose_name='ControlNumber')),
                ('date', models.DateField(null=True, verbose_name='Date Release')),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Branch')),
                ('motor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Motor')),
            ],
        ),
    ]
