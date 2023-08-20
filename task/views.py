from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Task,TaskLabel
from .serializers import TaskLabelSerializer,TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskLabelViewSet(viewsets.ModelViewSet):
    queryset = TaskLabel.objects.all()
    serializer_class = TaskLabelSerializer