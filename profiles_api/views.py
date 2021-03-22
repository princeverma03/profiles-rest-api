from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    '''
    Test APIview
    '''
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        '''
        Returns a list of API view features
        '''
        an_apiview = [
            'Uses HTTP method as functions (get, post, put, patch, delete)',
            'Is similar to a Django View',
            'Gives you the most control over the application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        '''
        Create a hello mesage withour name
        '''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello ! {name}'
            return Response({'message': message})

        else:
            return Response(serializer.errors,
                            status = status.HTTP_400_BAD_REQUEST
                            )
    def put(self, request, pk=None):
        '''
        Handle updating entire object (replace operation)
        '''
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        '''
        Handle partial update of an object (modify operation)
        '''
        return Response({'method' : 'PATCH'})

    def delete(self, request, pk=None):
        '''
        Delete an Object from DB
        '''
        return Response({'method': 'DELETE'})
