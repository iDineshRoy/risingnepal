from django.db import models
from django import forms

from domain.aggregates.student import StudentModel, StudentParentModel, ParentModel


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        exclude = [
            "version",
            "year_grade_section",
            "attendance",
            "parents",
            "student_parent",
        ]


class ParentForm(forms.ModelForm):
    class Meta:
        model = ParentModel
        exclude = ["version"]


class StudentParentForm(forms.ModelForm):
    class Meta:
        model = StudentParentModel
        fields = ["relationship"]
