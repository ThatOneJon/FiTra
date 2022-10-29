from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# import user authentication model from django
# create custom profile table,to store additional infos and use signals to auto create Profile on user creation


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    creation = models.DateField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username} created {self.creation}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance )
        instance.profile.save()

@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
        instance.profile.save()


class Workout(models.Model):
    workoutQualityChoices = [
        ('+', 'positive'),
        ('-', 'negative')
    ]
    workoutKind = [
        ("weight", "weightTraining"),
        ("cardio", "cardioTraining")
    ]
    workoutQuality = models.CharField(max_length = 200, choices = workoutQualityChoices, default = "+")
    date = models.DateField(auto_now_add = True)
    kind = models.CharField(max_length= 200, choices = workoutKind)

    def __str__(self):
        return f"{self.kind} from {self.date}"

#creation of an abstract Exercise class with specific weight and cardio classes inheriting
class Exercises(models.Model):
    workout = models.ForeignKey(Workout, on_delete = models.CASCADE)

    class Meta:
        abstract = True 

class WeightExercises(Exercises):
    exercise = models.CharField(max_length = 200) 
    weight = models.IntegerField()
    sets = models.IntegerField()
    repetitions = models.IntegerField()

    def __str__(self):
        return f"{self.exercise} from {self.workout.date}"

class CardioExercises(Exercises):
    kind = models.CharField(max_length = 200, default ="running")
    distance = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.kind} from {self.workout.date}"

#Used ADMIN INLINES to display the exercises inside corresponding Workout list!
