# Generated by Django 4.1.3 on 2022-11-15 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_ticket_booked_by_remove_ticket_ticket_from_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='assistant_manager',
        ),
        migrations.RemoveField(
            model_name='station',
            name='deputy_rpf',
        ),
        migrations.RemoveField(
            model_name='station',
            name='head_officer',
        ),
        migrations.RemoveField(
            model_name='station',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='station',
            name='rpf',
        ),
        migrations.AddField(
            model_name='station',
            name='station_master',
            field=models.CharField(default='', max_length=20),
        ),
    ]