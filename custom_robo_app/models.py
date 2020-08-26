from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomRobo(AbstractUser):
    homepage = models.URLField(blank=True, null=True)
    age = models.IntegerField(blank=True,null=True)