# Generated by Django 4.2 on 2024-07-19 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Static', '0011_coursedetails_filled_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecenter',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]