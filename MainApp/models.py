from django.db import models

class Member_dbdm(models.Model):
    user_id = models.CharField(max_length=32, unique=True, blank=False)
    user_pw = models.CharField(max_length=32, blank=False)
    user_name = models.CharField(max_length=32)
    user_address = models.CharField(max_length=256)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=64)
    join_date = models.DateTimeField('date joined')