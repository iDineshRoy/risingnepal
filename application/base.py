from typing import Any, Type
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db import models
from django import forms
from django.urls import path


class BaseView:
    model: Type[models.Model]
    form_class: Type[forms.ModelForm]
    context_object_name = None
    paginate_by = 10
    template_name = None
    success_url = None
    more_context: dict = {}
    ordering: list | None = ["-modified", "created"]

    def __init__(self, **kwargs):
        self.model = kwargs.pop("model", self.model)
        self.template_name = kwargs.pop("template_name", self.template_name)
        self.form_class = kwargs.pop("form_class", self.form_class)
        self.success_url = kwargs.pop("success_url", self.success_url)
        self.ordering = kwargs.pop("ordering", self.ordering)
        self.context_object_name = kwargs.pop(
            "context_object_name", self.context_object_name
        )
        self.more_context = kwargs.pop("more_context", self.more_context)
        super().__init__(**kwargs)

    def url_patterns(self):
        all_paths = []
        create = path(
            f"create_{str(self.model.__name__).lower()}/",
            CreateView.as_view(
                model=self.model,
                form_class=self.form_class,
                template_name="create.html",
                success_url=reverse_lazy(f"list_{str(self.model.__name__).lower()}"),
            ),
            name=f"create_{str(self.model.__name__).lower()}",
        )

        update = path(
            f"update_{str(self.model.__name__).lower()}/<int:pk>",
            UpdateView.as_view(
                model=self.model,
                form_class=self.form_class,
                template_name="create.html",
                success_url=reverse_lazy(f"list_{str(self.model.__name__).lower()}"),
            ),
            name=f"update_{str(self.model.__name__).lower()}",
        )

        class ListObjects(ListView):
            model = self.model
            more_context = self.more_context

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context.update(self.more_context)
                return context

        list = path(
            f"list_{str(self.model.__name__).lower()}/",
            ListObjects.as_view(
                model=self.model,
                context_object_name=self.context_object_name,
                paginate_by=10,
                ordering=self.ordering,
                template_name=self.template_name,
            ),
            name=f"list_{str(self.model.__name__).lower()}",
        )

        delete = path(
            f"delete_{str(self.model.__name__).lower()}/<int:pk>",
            DeleteView.as_view(
                model=self.model,
                template_name="delete.html",
                success_url=reverse_lazy(f"list_{str(self.model.__name__).lower()}"),
            ),
            name=f"delete_{str(self.model.__name__).lower()}",
        )

        all_paths.append(create)
        all_paths.append(update)
        all_paths.append(list)
        all_paths.append(delete)
        return all_paths
