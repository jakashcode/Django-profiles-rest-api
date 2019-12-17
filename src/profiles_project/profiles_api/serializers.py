from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing our APIView."""

    name=serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """ A serializer for out user profile object."""

    #defining a meta class that tells django rest framework
    #what fields we want to take from our models

    class Meta:

        model=models.UserProfile

        """ this tells django rest framework that this model serializer
        is going to be used with our user profile model"""

        fields=('id','email','name','password')

        """ what fields from out model we want to use in our serializer"""


        extra_kwargs={'password':{'write_only':True}}

        """ allow us to tell django rest framework special attributes we want
        to aplly to these fields"""
        """ you will nver beable to read the password through serializer,
        only write through serializer."""


    def create(self,validated_data):
        """ Create and return a new user."""

        user=models.UserProfile(

        email=validated_data['email'],
        name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
