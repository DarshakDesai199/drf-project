from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),

    path('employee/',views.Employees.as_view()),
    path('employee/<int:pk>/',views.EmployeeDetail.as_view()),
    path('employees/',views.EmployeesUsingMixIn.as_view()),
    path('employees/<int:pk>/',views.EmployeesUsingMixInDetails.as_view())
]

