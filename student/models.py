from django.db import models

# Create your models here.
class Student(models.Model):
    sname = models.CharField(max_length=30)
    semail = models.EmailField()
    sage = models.IntegerField()

    class Meta:
        db_table = 'student1'
       