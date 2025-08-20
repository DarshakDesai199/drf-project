from django.db import models

# Create your models here.
class Student(models.Model):
    students_id= models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=5)

    def __str__(self):
        return self.name