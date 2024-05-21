from django.db import models

# Create your models here.
class Dept(models.Model):
    dname=models.CharField(max_length=25)
    dloc=models.CharField(max_length=25)

    def __str__(self):
        return self.dname

class Employee(models.Model):
    ename=models.CharField(max_length=25)
    eage=models.IntegerField()
    dept=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename

