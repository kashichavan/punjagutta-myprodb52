from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()

    def __str__(self):
        return self.name

class Course(models.Model):
    course_name=models.CharField(max_length=50)
    students=models.ManyToManyField(Student)
