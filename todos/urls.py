from django.urls import path
from .views import TodoView, TodoDetailView
from rest_framework.routers import DefaultRouter
from django.urls import include

urlpatterns = [
  path('todos/', TodoView.as_view()),
  path('todos/<int:pk>', TodoDetailView.as_view())
]