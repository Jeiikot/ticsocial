from django.db import models
from django.contrib.auth.models import AbstractUser

class Person(AbstractUser):
    birthday = models.DateField(auto_now=False, auto_created=False, blank=True, null=True)
    id_type = models.CharField('ID Type', max_length=150,  blank=True, null=True)
    id_number = models.IntegerField('ID Number', default=0)