from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=50)
    master_password = serializers.CharField(max_length=50)

#
# class SiSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=50)
#     password = serializers.CharField(max_length=50)
#     email = serializers.CharField(max_length=50)
#     master_password = serializers.CharField(max_length=50)
