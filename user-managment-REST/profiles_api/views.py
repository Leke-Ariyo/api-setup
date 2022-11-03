from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

#allow user to see the entire list of obj (feeds) without being authenticated yet.
#from rest_framework.permissions import IsAuthenticatedOrReadOnly

#allow user to see the entire list of obj (feeds) only after being authenticated.
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and upating user profiles"""
    serializer_class = serializers.UserProfileSerializer

    #get all objects from db
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


#overwrite the default Login classes to display on Browser 
#so that we can test via Browser
#normally login module is not visible, now we attached this to View
class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


