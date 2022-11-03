from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id','name','password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'required': False,
                'style':{'input_type':'password'}
            }
        }


    #overwrite the default create function
    #so that password field will be encrypted instead of plain text
    def create(self,validated_data):
        """Create and return a new user"""
        print("USERS", validated_data)
        try:
            user = models.UserProfile.objects.create_user(
                name = validated_data['name'],
                password = validated_data['password'],
                id = validated_data['id'],
            )
        except:
            user = models.UserProfile.objects.create_user(
                name = validated_data['name'],
                id = validated_data['id'],
            )
        return user
