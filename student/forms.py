from typing import Any
from django.db import models
from django import forms

from domain.aggregates import Student, StudentParent, Parent, Bill
import nepali_datetime


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ["version", "active", "dob", "admitted_on_bs"]

    def clean_dob(self):
        dob_bs = self.cleaned_data["dob_bs"]
        if dob_bs is not None:
            dob_bs = nepali_datetime.date(
                year=dob_bs.year, month=dob_bs.month, day=dob_bs.day
            )
            dob_ad = dob_bs.to_datetime_date()
            return dob_ad

    def save(self, commit: bool = True):
        instance = super().save(commit=False)
        if instance.dob_bs:
            instance.dob = nepali_datetime.date(
                year=instance.dob_bs.year,
                month=instance.dob_bs.month,
                day=instance.dob_bs.day,
            ).to_datetime_date()
        if instance.admitted_on:
            instance.admitted_on_bs = nepali_datetime.date.from_datetime_date(
                instance.admitted_on
            )
        return super().save(commit)


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        exclude = ["version", "active"]


class StudentParentForm(forms.ModelForm):
    class Meta:
        model = StudentParent
        fields = ["student", "parent", "relationship"]
