# Generated by Django 4.1.3 on 2022-11-18 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seats',
            name='date',
            field=models.CharField(max_length=10),
        ),
    ]
