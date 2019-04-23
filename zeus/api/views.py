from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import CreateAPIView
from .serializers import UserCreationSerializers


class UserCreationApiView(CreateAPIView):
    serializer_class = UserCreationSerializers
