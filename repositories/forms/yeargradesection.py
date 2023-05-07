from domain.aggregates import YearGradeSection, YearGradeSectionStudent
from django import forms


class YearGradeSectionForm(forms.ModelForm):
    class Meta:
        model = YearGradeSection
        fields = ["year", "year_ad", "grade", "section", "description"]


class YearGradeSectionStudentForm(forms.ModelForm):
    class Meta:
        model = YearGradeSectionStudent
        fields = ["year_grade_section", "student"]
