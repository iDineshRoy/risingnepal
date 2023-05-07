from django.db import models
from django.contrib.auth.models import AbstractUser, User

from domain.aggregates.student import Student


class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_operator = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    class Meta:
        app_label = "users"
        db_table = "users"
