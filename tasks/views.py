from django.shortcuts import render
from .serializers import taskSerializer
from .models import Task
from rest_framework import viewsets
# Create your views here.

class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = taskSerializer