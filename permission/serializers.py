from rest_framework import serializers
from .models import Group


class SendSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    class Meta:
        model = Group
        fields = ['name', 'users']
