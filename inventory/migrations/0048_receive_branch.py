# Generated by Django 4.2.6 on 2023-11-16 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0047_repoout_branch_repoout_comaker_repoout_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='receive',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.branch'),
        ),
    ]