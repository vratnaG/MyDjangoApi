from rest_framework import serializers
from .models import students_collection


class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = students_collection
        fields = '__all__'
