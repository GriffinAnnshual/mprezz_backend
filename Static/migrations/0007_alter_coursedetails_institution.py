# Generated by Django 4.2 on 2024-06-08 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Static', '0006_coursedetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedetails',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Static.coursecenter'),
        ),
    ]