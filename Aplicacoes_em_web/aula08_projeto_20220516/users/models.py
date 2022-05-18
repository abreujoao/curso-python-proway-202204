from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date= models.DateField()

    class Meta:
        db_table='tb_profile'