from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """ Test API VIEW"""

    def get(self,request,format=None):

        an_apiview=[
        'Uses HTTP methods as function1 (get),post,patch,put,delete',
        'It is Similar to a traditional django view. ',
        'Gives youmost control over logic',
        'Is mapped manually to urls']

        return Response({'message':'Hello','an_apiview':an_apiview})
