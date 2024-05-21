from django.db import models

# Create your models here.
class Adhaar(models.Model):
    pass

class Person(models.Model):
    name = models.CharField(max_length=50)
    adhaar=models.OneToOneField(Adhaar,on_delete=models.CASCADE)
