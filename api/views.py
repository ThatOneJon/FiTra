from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProfileSerializer, UserSerializer, WorkoutSerializer, WeightExercisesSerializer
from fiTra.models import *

#import the Response class in order to parse the data to Str -> pass in native python, cannot handle models
#import serializers in Order to serialize Models -> pass models to response 
#import decorators for api_view 



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
        return Response({"first":"1"})
    except Workout.DoesNotExist:
        return Response({"ERROR" : "No Matching workout"})
    


