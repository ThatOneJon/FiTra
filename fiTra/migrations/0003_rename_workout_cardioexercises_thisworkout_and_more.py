# Generated by Django 4.1.2 on 2022-11-01 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiTra', '0002_rename_username_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardioexercises',
            old_name='workout',
            new_name='thisWorkout',
        ),
        migrations.RenameField(
            model_name='weightexercises',
            old_name='workout',
            new_name='thisWorkout',
        ),
    ]
