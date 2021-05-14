from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

