from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework import viewsets
from .student import Student


class StudentSerializedView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
