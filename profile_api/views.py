from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""
    def get(self,request,format=None):
        """resturn a list of ApiView features"""
        an_apiview = [
            'uses function get ,post ,put ,delete,patch',
            'is similar to a traditional django view',
            'Gives you the most control over you application logic',
            'is mapped manually to URLs',
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})