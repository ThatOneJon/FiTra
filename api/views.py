from cmath import log
import re
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from .serializers import ProfileSerializer, UserSerializer, WorkoutSerializer, WeightExercisesSerializer, CardioExerciseSerializer
from fiTra.models import *
from django.contrib.auth.decorators import login_required
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

#import the Response class in order to parse the data to Str -> pass in native python, cannot handle models
#import serializers in Order to serialize Models -> pass models to response 
#import decorators for api_view 
#default permission classes in settings -> always have to be logged in to see, change or delete data

# TOKEN CONFIG
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



#GETTING AP DATA --------------------------------------------- -->
@api_view(['GET'])
def api_Overview(request):
    api_Urls = {
    'FITRA API' : 'ENDPOINT OVERVIEW',
    'Create a new user' : 'createUser/',
    'Profile - can only access own' : 'profile/<str:pk>',
    'Edit your own profile' : 'editProfile/<str:pk>',
    'Delete your profile' : 'deleteProfile/<str:pk>', 
    'Create a new Workout for your user' : 'createWorkout/',
    
    'Show all Workouts' : 'allWorkouts/',

    'Edit your Workout with id' : 'workout/<str:pk>',
    'Create Exercise for a workout' : 'createExercise/<str:pk>',
    'Edit weight Exercise' : 'editExercise/weight/<str:pk>',
    'Edit cardio Exercise' : 'editExercise/cardio/<str:pk>',
    'Delete an Exercise' : 'deleteExercise/<str:pk>',
    'Delete a Workout with all its Exercises' : 'deleteWorkout/<str:pk>', 
    }
    return Response(api_Urls)

#this api view will return a user Profile and the serialized user data, fitting the profile 
@login_required
@api_view(['GET'])
def get_Profile_Data(request, pk):

    if request.user.is_authenticated:
        #getting the right one by primary key
        profiles = Profile.objects.get(id=pk)
        if profiles.user != request.user:
            raise PermissionDenied
        #serializing the USER object from one to one field --> See one to one field docu
        serializer2 = UserSerializer(profiles.user, many=False)
        #serializing the profile
        serializer = ProfileSerializer(profiles, many = False)
        #creating a tuple with the data
        data = (serializer.data, serializer2.data)
        #return as respones (parse)
        return Response(data)

    else:
        return Response({"Error" :"No auth"})

@login_required
@api_view(['GET'])
def get_Workout_Data(request, pk):    
    try:
        theWorkout = Workout.objects.get(id=pk)
        if theWorkout.owner != request.user:
            raise PermissionDenied
        serializerW = WorkoutSerializer(theWorkout, many=False)
        if theWorkout.kind == "weight":
            allExercises = theWorkout.weightWorkout.all()
            serializerT = WeightExercisesSerializer(allExercises, many = True)
            data = (serializerW.data, serializerT.data)
            return Response(data)
        elif theWorkout.kind == "cardio":
            allExercises = theWorkout.cardioWorkout.all() 
            serializerT = CardioExerciseSerializer(allExercises, many = True)

        else: 
            raise Workout.DoesNotExist

    except Workout.DoesNotExist:
        return Response({"ERROR" : "No Matching workout"})
@login_required
@api_view(['GET']) 
def get_all_Workouts(request):
    allTheWorkouts = Workout.objects.filter(owner = request.user)
    serializer = WorkoutSerializer(allTheWorkouts, many=True)
    return Response(serializer.data)


# POSTING AP DATA -------------------------------------------------- <------

@api_view(['POST'])
def generate_new_user(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

@login_required
@api_view(['POST'])
def generate_new_workout(request):
    serializer = WorkoutSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save(owner = request.user)
        return Response(serializer.data)

@login_required
@api_view(['POST'])
def generate_new_exercise(request, pk):
    #thisWorkout = Workout.objects.get(id=pk)
    if request.data.kind == "weight":
        serializer = WeightExercisesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    elif request.data.kind == "cardio":
        serializer = CardioExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

    else:
        return Response({"ERROR": "Exercise could not be saved!"})

@login_required
@api_view(['GET','POST'])
def edit_existing_weight_exercise(request, pk):
    exercise = WeightExercises.objects.get(id=pk)
    if exercise.workout.owner != request.user:
        raise PermissionDenied
    serializer=WeightExercisesSerializer(instance=exercise, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.data)

@login_required
@api_view(['GET','POST'])
def edit_existing_cardio_exercise(request, pk):
    exercise = CardioExercises.objects.get(id=pk)
    if exercise.workout.owner != request.user:
        raise PermissionDenied
    serializer=CardioExerciseSerializer(instance=exercise, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@login_required
@api_view(['GET','POST'])
def edit_existing_profile(request, pk):
    profile = Profile.objects.get(id =pk)
    if profile.user != request.user:
        raise PermissionDenied
    serializer=ProfileSerializer(instance=profile, data=request.data)
    if serializer.is_valid:
        serializer.save()
        return Response(serializer.data)

@login_required    
@api_view(['DELETE'])
def delete_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    if profile.user != request.user:
        raise PermissionDenied
    user = profile.user
    user.delete()
    profile.delete()

@login_required
@api_view(['DELETE'])
def delete_exercise(request, pk):
    pass    

@login_required
@api_view(['DELETE'])
def delete_workout(request, pk):
    workout = Workout.objects.get(id=pk)
    if workout.owner != request.user:
        raise PermissionDenied
    workout.delete()
