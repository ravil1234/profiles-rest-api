from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers

# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """resturn a list of ApiView features"""
        an_apiview = [
            'uses function get ,post ,put ,delete,patch',
            'is similar to a traditional django view',
            'Gives you the most control over you application logic',
            'is mapped manually to URLs',
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
    def post(self,request):
         """create a hello message with our name"""
         serializer=self.serializer_class(data=request.data)
         
         if serializer.is_valid():
             name = serializer.validated_data.get('name') 
             message = f'Hello {name}'
             return Response({'message':message})   
         else :
             return Response(
                 serializer.errors,
                 status=status.HTTP_400_BAD_REQUEST
                 ) 
    def put(self,request,id=None):
         """handle updating an object"""
         return Response({'message':'PUT REQUEST'}) 

    def patch(self,request,id=None):
         """handle partially updating an object"""
         return Response({'message':'PATCH REQUEST'})

    def delete(self,request,id=None):
         """handle updating an object"""
         return Response({'message':'Delete Request'})
