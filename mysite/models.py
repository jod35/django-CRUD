from django.db import models

class Position(models.Model):
    position=models.CharField(max_length=200)

class Employee(models.Model):
    full_name=models.CharField(max_length=200)
    emp_code=models.CharField(max_length=200)
    mobile=models.CharField(max_length=200)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)
