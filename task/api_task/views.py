from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task, Project
from rest_framework import viewsets, permissions
from .serializers import NewTaskSerializer, ProjectSerializer, UserSerializer
# from .permissions import IsOwnerOrReadOnly

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """This viewset automatically provides `list`,
     `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NewTaskViewSet(viewsets.ModelViewSet):
    """This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Task.objects.all()
    serializer_class = NewTaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ProjectViewSet(viewsets.ModelViewSet):
    """This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.
        """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
