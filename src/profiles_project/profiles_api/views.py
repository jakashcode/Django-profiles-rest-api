from django.shortcuts import render
from . import models

from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status

from . import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class HelloApiView(APIView):
    """ Test API VIEW"""
    serializer_class=serializers.HelloSerializer



    def get(self,request,format=None):

        an_apiview=[
        'Uses HTTP methods as function1 (get),post,patch,put,delete',
        'It is Similar to a traditional django view. ',
        'Gives youmost control over logic',
        'Is mapped manually to urls']

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """ create a hello message with our name."""

        serializer=serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)

            return Response({'message':message})
        else:
            return(
            Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            )

    def put(self,request,pk=None):

        """ Handles updating object"""
        return Response({"method":'put'})

    def patch(self,request,pk=None):

        """ Patch request, only update fields provided in the request"""
        return Response({"method":'patch'})

    def delete(self,request,pk=None):
        """ Deletes an object"""
        return Response({"method":'delete'})


class HelloViewSet(viewsets.ViewSet):

    """ Test API VIEWSET"""
    serializer_class=serializers.HelloSerializer

    def list(self,request):
        """ Return Hello Message"""

        a_viewset=[
        'Uses actions (list,create,retrieve,update,partial_update)',
        'Automatically maps to urls using routers',
        'Provides more functionality with less code'
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self,request):

        """Create a hello message."""

        serializer=serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """ handles getting an object by it's id"""
        return Response({"method":'GET'})

    def update(self,request,pk=None):
        """ Handles updating an object"""
        return Response({"method":'PUT'})

    def partial_update(self,request,pk=None):
        """ Updating some fields of an object"""
        return Response({"method":'PATCH'})

    def destroy(self,request,pk=None):
        """ Handles removing an object"""
        return Response({"method":'delete'})



class UserProfileViewset(viewsets.ModelViewSet):
    """ Handles creating and Updating profiles."""

    serializer_class=serializers.UserProfileSerializer

    queryset=models.UserProfile.objects.all()
    """ listing out all the objects from out database."""

    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)

    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email')

class LoginViewSet(viewsets.ViewSet):
    """ Checks email and password and return an auth token."""

    serializer_class=AuthTokenSerializer

    def create(self,request):
        """ Use the ObtainAuthToken APIView to validate and create token."""

        return ObtainAuthToken().post(request)

class UserProfileFeedViewset(viewsets.ModelViewSet):
    """ Handles Creating, reading, and updating profile feed items."""

    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.ProfileFeedItemSerializer
    queryset=models.ProfileFeedItem.objects.all()
    permission_classes=(permissions.PostOwnStatus,IsAuthenticated)

    def perform_create(self,serializer):
        """ Sets the user_profile to the logged in user."""

        serializer.save(user_profile=self.request.user)
