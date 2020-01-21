from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(blank=True, unique=True, max_length=255)

    def __str__(self):
        return self.email