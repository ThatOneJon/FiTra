# Generated by Django 4.1.2 on 2022-11-01 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fiTra', '0006_alter_cardioexercises_cardioworkout_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardioexercises',
            name='cardioWorkout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cardioWorkout', to='fiTra.workout'),
        ),
        migrations.AlterField(
            model_name='weightexercises',
            name='weightWorkout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weightWorkout', to='fiTra.workout'),
        ),
    ]
