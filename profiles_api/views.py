from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Retourne une liste de fonctionnalités"""
        an_apiview = [
            'Use  HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditionnal Django view',
            'Gives you a total control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello !', 'an_apiview': an_apiview})

    def post(self, request):
        """Crée un message Hello avec notre nom"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """update an object"""
        return Response({'method':'PUT'})
    

    def patch(self, request, pk=None):
        """partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})
