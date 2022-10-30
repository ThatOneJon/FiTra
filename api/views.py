from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProfileSerializer
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


@api_view(['GET'])
def get_Profile_Data(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many = True)
    return Response(serializer.data)