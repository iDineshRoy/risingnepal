from typing import Type
from dal import autocomplete
from django.db import models
from django.db.models import Q


class AutoComplete(autocomplete.Select2QuerySetView):
    model = Type[models.Model]
    filter_params = None

    def __init__(self, model=None):
        if model is not None:
            self.model = model

    def get_queryset(self):
        q_objects = Q()

        for key, value in self.filter_params.items():
            q_objects |= Q(**{key: self.q})

        qs = self.model.objects.all()
        if self.q:
            qs = qs.filter(q_objects)
        return qs
