# Generated by Django 3.0.5 on 2024-05-31 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userauthentication', '0004_auto_20240529_2302'),
        ('mygallary', '0003_auto_20240529_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpost',
            name='user',
            field=models.ForeignKey(default='this is default', on_delete=django.db.models.deletion.CASCADE, to='userauthentication.user_db'),
        ),
    ]
