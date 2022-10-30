from fiTra.models import *
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'firstname', 'lastname')




class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        print(Profile.user)
        #fields = '__all__'
        fields = ('creation', 'user',)