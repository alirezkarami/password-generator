from rest_framework import serializers


class PasswordSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    created_at = serializers.DateTimeField()


class PasswordsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)

