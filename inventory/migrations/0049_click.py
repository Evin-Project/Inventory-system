# Generated by Django 4.2.6 on 2023-11-17 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0048_receive_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='click',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_click', models.BooleanField(default=False)),
            ],
        ),
    ]
