# Generated by Django 4.1.3 on 2022-11-18 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_remove_train_classes_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('seats', models.IntegerField()),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.train')),
            ],
        ),
    ]