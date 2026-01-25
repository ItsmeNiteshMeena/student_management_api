from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    college=models.CharField(max_length=20,default="UIT")
    def __str__(self):
        return self.name
