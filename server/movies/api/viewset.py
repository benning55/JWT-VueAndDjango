from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
import jwt
from .serializers import *


@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            user.groups.add(Group.objects.get(name='client'))
            data['response'] = "Successfully registered"
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)


@api_view(['GET', ])
def user_view(request):

    if request.method == 'GET':
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


