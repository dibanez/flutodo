from .models import Todo
from django.contrib.auth.models import User
from main.serializers import UserSerializer
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer


class TodoSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Todo
        fields = ['id', 'name', 'isComplete', 'user']

    def create(self, validated_data):
        user = User.objects.first()
        todo = Todo(name=validated_data.get("name"), user=user)
        todo.save()
        return validated_data

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return validated_data
