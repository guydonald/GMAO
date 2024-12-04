from django.db import models
from django.contrib.auth.models import AbstractUser, Group

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.username

    