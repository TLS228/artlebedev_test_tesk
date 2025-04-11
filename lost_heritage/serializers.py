from rest_framework import serializers
from .models import LostObject


class LostObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostObject
        fields = '__all__'
