from django.db import models
import datetime

class RegisterDateModel(models.Model):
    name = models.CharField(max_length=10, null=True)
    lastname = models.CharField(max_length=10, null=True)
    email = models.EmailField(default="None", null=True, blank=True)
    phone = models.CharField(max_length=15, null=True)
    description = models.CharField(max_length=30, null=True, blank=True, default="anything")
    register = models.DateField(auto_now_add=datetime.datetime.now())
    calendar = models.DateField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'app_registerdate'