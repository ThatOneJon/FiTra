from fiTra.models import *
from rest_framework import serializers
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):
    #hier wird Foreign key Beziehung zu workouts reversed genutzt, um alle workouts anzuzeigen(auch api view!)<<<<<<<<<<<<<<<<<
    workouts = serializers.PrimaryKeyRelatedField(many=True, queryset=Workout.objects.all())
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'workouts')
        extra_kwargs = {'password':{'write_only':True}}

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        #fields = '__all__'
        fields = ('creation', 'user',)

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields='__all__'

class WeightExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightExercises
        fields='__all__'

class CardioExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model=CardioExercises
        fields='__all__'

class LoginSerializer(serializers.ModelSerializer):
    pass