from fiTra.models import *
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')




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