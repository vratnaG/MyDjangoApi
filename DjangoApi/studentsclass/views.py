from django.shortcuts import render
from .serializers import StudentsClassSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from students.models import students_collection
# Create your views here.


class StudentListClass(generics.GenericAPIView):

    def get(self, request):
        query = students_collection.objects.all()
        serializer = StudentsClassSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    serializer_class = StudentsClassSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailClass(generics.GenericAPIView):

    def get_object(self, id):
        try:
            return students_collection.objects.get(id=id)
        except students_collection.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        data = self.get_object(id)
        serializer = StudentsClassSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    serializer_class = StudentsClassSerializer

    def put(self, request, id):
        data = self.get_object(id)
        serializer = self.serializer_class(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        data = self.get_object(id)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
