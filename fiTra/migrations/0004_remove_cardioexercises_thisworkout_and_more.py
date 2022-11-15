# Generated by Django 4.1.2 on 2022-11-01 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fiTra', '0003_rename_workout_cardioexercises_thisworkout_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardioexercises',
            name='thisWorkout',
        ),
        migrations.RemoveField(
            model_name='weightexercises',
            name='thisWorkout',
        ),
        migrations.AddField(
            model_name='cardioexercises',
            name='cardioWorkout',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='cardioWorkout', to='fiTra.workout'),
        ),
        migrations.AddField(
            model_name='weightexercises',
            name='weightWorkout',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='weightWorkout', to='fiTra.workout'),
        ),
    ]
