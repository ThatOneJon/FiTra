from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from .serializers import ProfileSerializer, UserSerializer, WorkoutSerializer, WeightExercisesSerializer, CardioExerciseSerializer
from fiTra.models import *


#import the Response class in order to parse the data to Str -> pass in native python, cannot handle models
#import serializers in Order to serialize Models -> pass models to response 
#import decorators for api_view 


#GETTING AP DATA --------------------------------------------- -->
@api_view(['GET'])
def api_Overview(request):
    api_Urls = {
        "GET_Profile" : "one",
        "CREATE_Profile" : "two",
        "DELETE_Profile" :"three",
        "GET_Workout" : "four",
        "CREATE_Workout" : "five",
        "DELETE_Workout" : "six"
    }
    return Response(api_Urls)

#this api view will return a user Profile and the serialized user data, fitting the profile 
@api_view(['GET'])
def get_Profile_Data(request, pk):
    if request.user.is_authenticated:
        #getting the right one by primary key
        profiles = Profile.objects.get(id=pk)
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

@api_view(['GET'])
def get_Workout_Data(request, pk):
    try:
        theWorkout = Workout.objects.get(id=pk)
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
    
# POSTING AP DATA -------------------------------------------------- <------

@api_view(['POST'])
def generate_new_user(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)


@api_view(['POST'])
def generate_new_workout(request):
    serializer = WorkoutSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)


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

@api_view(['POST'])
def edit_existing_weight_exercise(request, pk):
    exercise = WeightExercises.objects.get(id=pk)
    serializer=WeightExercisesSerializer(instance=exercise, data=request.data)
    if serializer.is_valid:
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
def edit_existing_cardio_exercise(request, pk):
    exercise = CardioExercises.objects.get(id=pk)
    serializer=CardioExerciseSerializer(instance=exercise, data=request.data)
    if serializer.is_valid:
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
def edit_existing_profile(request, pk):
    profile = Profile.objects.get(id =pk)
    serializer=ProfileSerializer(instance=profile, data=request.data)
    if serializer.is_valid:
        serializer.save()
        return Response(serializer.data)
        
@api_view(['DELETE'])
def delete_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    user = profile.user
    user.delete()
    profile.delete()

@api_view(['DELETE'])
def delete_exercise(request, pk):
    pass    

@api_view(['DELETE'])
def delete_workout(request, pk):
    workout = Workout.objects.get(id=pk)
    workout.delete()
