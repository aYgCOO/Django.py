# Generated by Django 3.0.5 on 2024-04-08 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practiceapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
