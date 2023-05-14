from domain.aggregates import Fee, FeeStudent
from django import forms


class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ["fee_type", "amount", "year_grade_section", "description"]


class FeeStudentForm(forms.ModelForm):
    class Meta:
        model = FeeStudent
        fields = ["year_grade_section_student", "fee", "discount", "fee_date"]
