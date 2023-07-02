from django.db import models


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 255)
    age = models.IntegerField()
    email = models.CharField(max_length = 255)
    number = models.CharField(max_length = 255)
    employee_branch = models.ForeignKey('Branch', on_delete=models.CASCADE)

class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 255)
    building_number = models.CharField(max_length = 255)
    street = models.CharField(max_length = 255)
    area = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    country = models.CharField(max_length = 255)
    manager = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True)