from django.shortcuts import render
from rest_framework import viewsets, permissions
from main.models import Task
from main.serializers import TaskSerializer
# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows tasks to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
