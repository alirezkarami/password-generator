from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Password
from .serializers import PasswordSerializer, PasswordsSerializer


# Create your views here.

@api_view(['GET'])
def create(request):
    name = request.GET.get('name')
    password = request.GET.get('password')
    create_model = Password(name=name, password=password)
    create_model.save()
    serializer_password = PasswordSerializer(create_model)
    return Response(serializer_password.data)


@api_view(['GET'])
def read(request):
    passwords = Password.objects.all()
    passwords_serializer = PasswordsSerializer(passwords, many=True)
    return Response(passwords_serializer.data)


@api_view(['GET'])
def update(request):
    password = request.GET.get('password')
    nid = request.GET.get('id')
    edit_password = Password.objects.get(id=nid)
    edit_password.password = password
    edit_password.save()
    serializer_password = PasswordSerializer(edit_password)
    return Response(serializer_password.data)
