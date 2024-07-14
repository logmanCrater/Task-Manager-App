from rest_framework import serializers
from .models import Task, StatusChangeRequest
from django.contrib.auth.models import User, Group

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class StatusChangeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusChangeRequest
        fields = '__all__'
