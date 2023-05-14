from django.db import models
from django.utils.translation import gettext_lazy as _


# Base entity model
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True)
    version = models.PositiveIntegerField(default=1)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


# Base junction model
class BaseJunctionModel(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True)
    version = models.PositiveIntegerField(default=1)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
