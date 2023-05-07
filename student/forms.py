from typing import Any
from django.db import models
from django import forms

from domain.aggregates import Student, StudentParent, Parent, Bill
import nepali_datetime


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = [
            "version",
            "year_grade_section",
            "attendance",
            "parents",
            "student_parent",
            "active",
            "dob",
            "admitted_on",
        ]

    def clean_dob(self):
        dob_bs = self.cleaned_data["dob_bs"]
        if dob_bs is not None:
            dob_bs = nepali_datetime.date(
                year=dob_bs.year, month=dob_bs.month, day=dob_bs.day
            )
            dob_ad = dob_bs.to_datetime_date()
            return dob_ad

    def clean_admitted_on(self):
        admitted_on_bs = self.cleaned_data["admitted_on_bs"]
        if admitted_on_bs is not None:
            admitted_on_bs = nepali_datetime.date(
                year=admitted_on_bs.year,
                month=admitted_on_bs.month,
                day=admitted_on_bs.day,
            )
            admitted_on_ad = admitted_on_bs.to_datetime_date()
            return admitted_on_ad

    def save(self, commit: bool = True):
        instance = super().save(commit=False)
        instance.dob = instance.dob
        instance.admitted_on = instance.admitted_on
        return super().save(commit)


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        exclude = ["version", "active"]


class StudentParentForm(forms.ModelForm):
    class Meta:
        model = StudentParent
        fields = ["student", "parent", "relationship"]
