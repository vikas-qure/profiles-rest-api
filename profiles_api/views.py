from rest_framework.views import APIView
from rest_framework.views import Response

class HelloApiView(APIView):
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'hello!', 'an_apiview': an_apiview})