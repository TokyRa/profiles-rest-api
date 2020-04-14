from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Retourne une liste de fonctionnalités"""
        an_apiview = [
            'Use  HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditionnal Django view',
            'Gives you a total control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello !', 'an_apiview': an_apiview})
