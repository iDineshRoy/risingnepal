from typing import Any, Dict
import nepali_datetime

from django.shortcuts import render
from django.db.models import F
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from domain.aggregates import Fee, FeeStudent


from repositories.forms import FeeForm, FeeStudentForm

from application.base import BaseView


# ---------------------------------------------------- #


class FeeView(BaseView):
    model = Fee
    form_class = FeeForm
    context_object_name = "objects"
    template_name = "list_fees.html"


class FeeStudentView(BaseView):
    model = FeeStudent
    form_class = FeeStudentForm
    context_object_name = "objects"
    template_name = "list_feestudent.html"
    ordering = ["-fee_date", "-modified", "-created"]
