from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import students_collection
from .serializers import StudentsSerializer
from rest_framework.response import Response


class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentsSerializer
    queryset = students_collection.objects.all()

    def perform_create(self, serializer):
        return serializer.save()

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = StudentsSerializer(queryset, many=True)
        return Response(serializer.data)


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentsSerializer
    queryset = students_collection.objects.all()
    lookup_field = 'id'

    def perform_create(self, serializer):
        return serializer.save()
