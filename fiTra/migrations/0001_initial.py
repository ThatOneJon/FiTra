# Generated by Django 4.1.2 on 2022-10-29 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workoutQuality', models.CharField(choices=[('+', 'positive'), ('-', 'negative')], default='+', max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('kind', models.CharField(choices=[('weight', 'weightTraining'), ('cardio', 'cardioTraining')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WeightExercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.CharField(max_length=200)),
                ('weight', models.IntegerField()),
                ('sets', models.IntegerField()),
                ('repetitions', models.IntegerField()),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fiTra.workout')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation', models.DateField(auto_now_add=True)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CardioExercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(default='running', max_length=200)),
                ('distance', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fiTra.workout')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
