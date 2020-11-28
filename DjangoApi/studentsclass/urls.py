from django.urls import path
from .views import StudentListClass, StudentDetailClass

urlpatterns = [
    path('', StudentListClass.as_view(), name='studentlistclass'),
    path('<id>', StudentDetailClass.as_view(), name='studentdetailclass'),
]
