from django.db import models

# Create your models here.


class students_collection(models.Model):
    fullname = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    course_of_study = models.CharField(max_length=60)
    year = models.IntegerField()
    gpa = models.FloatField()
