from django.urls import path
from .views import StudentList, StudentDetail

urlpatterns = [
    path('', StudentList.as_view(), name='studentlist'),
    path('<id>', StudentDetail.as_view(), name='studentdetail'),
]
