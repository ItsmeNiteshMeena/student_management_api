from django.urls import path
from .views import student_list_create, student_detail

urlpatterns = [
    path('students/', student_list_create),
    path('students/<int:id>/', student_detail),
]
