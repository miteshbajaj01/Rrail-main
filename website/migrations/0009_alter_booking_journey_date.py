# Generated by Django 4.1.3 on 2022-11-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_seats_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='journey_date',
            field=models.CharField(max_length=10),
        ),
    ]
