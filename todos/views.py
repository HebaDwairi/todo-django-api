from django.shortcuts import render
from django.http import HttpResponse
from .serializers import TodoSerializer
from rest_framework import status, permissions
from .models import Todo
from rest_framework import viewsets
from .permissions import IsOwner
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


class TodoView(APIView):
  permission_classes = (permissions.IsAuthenticated, IsOwner)

  def get(self, request):
    todos = Todo.objects.filter(user=request.user)
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailView(APIView):
  permission_classes = (permissions.IsAuthenticated, IsOwner)

  def get_object(self, pk):
    todo = get_object_or_404(Todo, pk=pk, user=self.request.user)
    self.check_object_permissions(self.request, todo)
    return todo

  def get(self, request, pk):
    todo = self.get_object(pk)
    serializer = TodoSerializer(todo)
    return Response(serializer.data)
  
  def put(self, request, pk):
    todo = self.get_object(pk)
    serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    todo = self.get_object(pk)
    todo.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)


'''
# using ModelViewSet instead
class TodoViewSet(viewsets.ModelViewSet):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer
  permission_classes = (permissions.IsAuthenticated, IsOwner)

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)
  
  def get_queryset(self):
    return self.queryset.filter(user=self.request.user)

'''