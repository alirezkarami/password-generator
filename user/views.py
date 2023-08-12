from rest_framework.decorators import api_view
from .models import UserCust
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


# Create your views here.
@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    master_password = request.data.get('master_password')
    data_user = UserCust(username=username, email=email, master_password=master_password)
    data_user.set_password(password)
    data_user.save()
    serializer_user = UserSerializer(data_user)
    return Response(serializer_user.data)


@api_view(['GET'])
def see_user(request):
    all_user = UserCust.objects.all()
    se_all_user = UserSerializer(all_user, many=True)
    return Response(se_all_user.data)


@api_view(['PUT'])
def edit_pass(request):
    old_username = request.data.get('old_username')

    edit_user = UserCust.objects.get(username=old_username)




