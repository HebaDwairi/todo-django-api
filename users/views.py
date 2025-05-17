from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, permissions
from .serializers import userSerializer

class RegisterView(generics.CreateAPIView):
  serializer_class = userSerializer
  permission_classes = (permissions.AllowAny,)
  