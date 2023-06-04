from typing import Any, Dict
import nepali_datetime

from django.shortcuts import render
from django.db.models import F
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from domain.aggregates import Fee, FeeStudent, Bill


from repositories.forms import FeeForm, FeeStudentForm, BillForm

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


class BillView(BaseView):
    model = Bill
    form_class = BillForm
    context_object_name = "bills"
    template_name = "list_bill.html"
    ordering = ["-modified", "-created"]
