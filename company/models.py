from django.db import models

# Create your models here.
class role(models.Model):
    role_name =  models.CharField(max_length=100)
    class Meta:
        db_table = 'role'

class department(models.Model):
    department_name = models.CharField(max_length=100)
    class Meta:
        db_table = 'department'
       


class employee(models.Model):
    role_id = models.ForeignKey(role, on_delete=models.CASCADE)
    department_id = models.ForeignKey(department, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    class Meta:
        db_table = 'employee'
       


       
