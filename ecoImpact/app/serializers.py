from rest_framework import serializers
from .models import Testing


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testing
        fields = '__all__'

