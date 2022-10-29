from django.contrib import admin
from fiTra.models import *

# Register your models here.


class ExercisesInline(admin.TabularInline):
    model = WeightExercises


class WorkoutAdmin(admin.ModelAdmin):
    inlines = [
        ExercisesInline
    ]

admin.site.register(Profile)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(WeightExercises)
