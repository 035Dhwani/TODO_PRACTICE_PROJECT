from django.db import models

# Create your models here.
class user(models.Model):
    uname = models.CharField(max_length=30)
    uage = models.IntegerField()
    uemail = models.EmailField()
    ucontact = models.IntegerField()
    class Meta:
        db_table = 'user1'
       