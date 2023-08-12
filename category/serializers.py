from rest_framework import serializers
from .models import Category


class SendSerializer(serializers.ModelSerializer):
    pass_id = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'pass_id']
