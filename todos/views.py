from django.shortcuts import render
from django.http import HttpResponse
from .serializers import TodoSerializer
from rest_framework import generics, permissions
from .models import Todo
from rest_framework import viewsets
from .permissions import IsOwner

class TodoViewSet(viewsets.ModelViewSet):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer
  permission_classes = (permissions.IsAuthenticated, IsOwner)

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)
  
  def get_queryset(self):
    return self.queryset.filter(user=self.request.user)
