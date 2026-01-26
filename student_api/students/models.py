from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    college=models.CharField(max_length=20,null=True)
    city=models.CharField(max_length=20,null=True)
    mobile=models.IntegerField(max_length=10,null=True)
    address=models.CharField(max_length=20,null=True)
    skills=models.TextField(max_length=30,null=True)
    def __str__(self):
        return self.name
