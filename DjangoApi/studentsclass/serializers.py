from rest_framework import serializers
from students.models import students_collection


class StudentsClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = students_collection
        fields = '__all__'
