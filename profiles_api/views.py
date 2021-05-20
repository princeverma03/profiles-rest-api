from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


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


class HelloViewSet(viewsets.ViewSet):
    '''
    Test Api Viewset
    '''
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        '''
        return a Hello Message
        '''
        a_viewset = ['uses action list, create, retrieve,update,partial-update,destroy',\
                     'Automatically maps to urls using Routers',\
                     'provides more functionality with less code',\
                    ]
        return Response({'message':'Hello !',
                         'a_viewset':a_viewset
                        })

    def create(self, request):
        '''
        Create a Hello message
        '''
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello {}'.format(name)

            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status= status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk= None):
        '''
        Handle getting an object
        '''
        return Response({'http_method':'GET'})

    def update(self, request, pk= None):
        '''
        Handle updating entire object
        '''
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk= None):
        '''
        Handle updating a part of object
        '''
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk= None):
        '''
        Handle deleting an object
        '''
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    '''
    Handle creating objects and updating them
    '''
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
