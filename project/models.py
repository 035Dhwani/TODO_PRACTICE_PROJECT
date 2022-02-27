from django.db import models
from generic.models import BaseField

# Create your models here.
class Appearence(models.Model):
    appearence_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'appearence'

class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=8)
    user_contct = models.IntegerField()
    appearence_name = models.ForeignKey(Appearence, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user'

class Status(models.Model):
    status_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'status'
      
class ProjectDetail(BaseField):
    project_title = models.CharField(max_length=50)
    project_description = models.CharField(max_length=250)
    project_technology = models.CharField(max_length=50)
    estimatedHours = models.IntegerField()
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)

    class Meta:
        db_table = 'project_detail'
       



       
        
