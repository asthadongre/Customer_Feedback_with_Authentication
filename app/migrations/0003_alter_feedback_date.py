# Generated by Django 3.2.2 on 2021-06-20 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210620_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
