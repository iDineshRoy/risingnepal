from django.db import models
from typing import Type, List


class BaseRepository:
    model: Type[models.Model]

    def __init__(self, model=None):
        if model is not None:
            self.model = model

    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def get(self, **kwargs):
        return self.model.objects.get(**kwargs)

    def update(self, obj, **kwargs):
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()

    def delete(self, obj):
        obj.delete()

    def get_all(self):
        return self.model.objects.all().order_by("-created")

    def filter(self, **kwargs):
        return self.model.objects.filter(**kwargs)

    def get_or_create(self, **kwargs):
        return self.model.objects.get_or_create(**kwargs)

    def bulk_create(self, objs):
        return self.model.objects.bulk_create(objs)

    def bulk_update(self, objs, fields):
        return self.model.objects.bulk_update(objs, fields)

    def bulk_delete(self, **kwargs):
        return self.model.objects.filter(**kwargs).delete()

    def count(self, **kwargs):
        return self.model.objects.filter(**kwargs).count()

    def exists(self, **kwargs):
        return self.model.objects.filter(**kwargs).exists()

    def annotate(self, **kwargs):
        return self.model.objects.annotate(**kwargs)

    def order_by(self, *args):
        return self.model.objects.order_by(*args)

    def values(self, *args):
        return self.model.objects.values(*args)


class BaseJunctionRepository:
    junction_model: Type[models.Model]
    left_model: Type[models.Model]
    right_model: Type[models.Model]

    def create(
        self, left_data: dict, right_data: dict, junction_data: dict = None
    ) -> models.Model:
        left_instance = self.left_model.objects.create(**left_data)
        right_instance = self.right_model.objects.create(**right_data)
        if junction_data is not None:
            junction_data.update(
                {
                    f"{self.left_model.__name__.lower().rstrip('model')}": left_instance,
                    f"{self.right_model.__name__.lower().rstrip('model')}": right_instance,
                }
            )
            junction_instance = self.junction_model.objects.create(**junction_data)
        else:
            junction_instance = self.junction_model.objects.create(
                **{
                    f"{self.left_model.__name__.lower().rstrip('model')}": left_instance,
                    f"{self.right_model.__name__.lower().rstrip('model')}": right_instance,
                }
            )
        return junction_instance

    def get(self, **kwargs) -> models.Model | None:
        return self.junction_model.objects.first(**kwargs)

    def fetch_left_and_right(self, **kwargs):
        left_q = self.left_model.objects.all().order_by("-created")
        return left_q

    def fetch(self, **kwargs):
        query = self.junction_model.objects.all(**kwargs).order_by("-created")
        return query

    def filter(self, **kwargs) -> List[models.Model]:
        return list(self.junction_model.objects.filter(**kwargs).order_by("-created"))

    def get_or_create(self, defaults: dict = None, **kwargs) -> (models.Model, bool):
        left_instance, left_created = self.left_model.objects.get_or_create(
            **kwargs.pop(f"{self.left_model.__name__.lower().rstrip('model')}_data"),
            defaults=defaults,
        )
        right_instance, right_created = self.right_model.objects.get_or_create(
            **kwargs.pop(f"{self.right_model.__name__.lower().rstrip('model')}_data"),
            defaults=defaults,
        )
        junction_defaults = {
            f"{self.left_model.__name__.lower().rstrip('model')}": left_instance,
            f"{self.right_model.__name__.lower().rstrip('model')}": right_instance,
        }
        if defaults:
            junction_defaults.update(defaults)
        junction_instance, junction_created = self.junction_model.objects.get_or_create(
            **kwargs, defaults=junction_defaults
        )
        return junction_instance, left_created or right_created or junction_created
