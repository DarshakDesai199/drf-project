from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def students(request):
    student = [{"name":"Darshak Desai","age":"23","role":"Developer"}]
    return HttpResponse(student)