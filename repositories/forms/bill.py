from domain.aggregates import Fee, FeeStudent, Bill, StudentParent
from django import forms
from django_select2 import forms as s2forms


class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ["fee_type", "amount", "year_grade_section", "description"]


class FeeStudentForm(forms.ModelForm):
    class Meta:
        model = FeeStudent
        fields = ["year_grade_section_student", "fee", "discount", "fee_date"]


class FeeStudentWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = ["fee__fee_type__icontains"]


class StudentParentWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "student__first_name__icontains",
        "parent__first_name__icontains",
        "parent__last_name__icontains",
    ]


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ["fee_student", "student_parent", "due_date", "status"]
        widgets = {
            "fee_student": FeeStudentWidget,
            "student_parent": StudentParentWidget,
        }
