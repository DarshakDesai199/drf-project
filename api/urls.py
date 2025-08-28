from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employeeViewSets', views.EmployeeViewSet, basename='employee')
router.register('employeeModelViewSets', views.EmployeeModelViewSet, basename='employeeModel')

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),

    path('employee/', views.Employees.as_view()),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view()),

    path('employees/', views.EmployeesUsingMixIn.as_view()),
    path('employees/<int:pk>/', views.EmployeesUsingMixInDetails.as_view()),

    path('employeeGenerics/', views.EmployeeGenerics.as_view()),
    path('employeeGenerics/<int:pk>/', views.EmployeeGenericsDetails.as_view()),
    path('', include(router.urls))
]
