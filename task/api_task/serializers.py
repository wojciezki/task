from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task, Project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password',
                  'last_login', 'date_joined',)
        write_only_fields = ('password',)


class NewTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(queryset=Task.objects.all(),
                                                view_name='task-detail',
                                                many=True)

    class Meta:
        model = Project
        fields = ('name', 'owner', 'description', 'tasks')
