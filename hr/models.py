from django.db import models


class Employee(models.Model):
    fullname = models.CharField(max_length=30)
    title = models.CharField(max_length=20)
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.fullname}  - {self.title} - {self.salary}"


class Passenger:
    def __init__(self,name,age):
        self.name = name
        self.age = age

