import nepali_datetime

from django.db import models

from domain.aggregates.base import BaseModel, BaseJunctionModel
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Student(BaseModel):
    # This contains the personal details about the students
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(blank=True, null=True)
    roll_number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    admitted_on = models.DateField(blank=True, null=True)
    year_grade_section = models.ForeignKey(
        "YearGradeSection", on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_dob_bs(self):
        dob_bs = nepali_datetime.date.from_datetime_date(self.dob)
        return dob_bs

    class Meta:
        db_table = "students"
        app_label = "student"


class YearGradeSection(BaseModel):
    year = models.IntegerField(
        validators=[MinLengthValidator(4), MaxLengthValidator(4)], blank=True, null=True
    )
    year_ad = models.IntegerField(
        validators=[MinLengthValidator(4), MaxLengthValidator(4)], blank=True, null=True
    )
    grade = models.CharField(max_length=20, blank=True, null=True)
    section = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.year} {self.grade} {self.section}"

    class Meta:
        unique_together = ("year", "grade", "section")
        db_table = "year_grade_section"
        app_label = "student"


class YearGradeSectionStudent(BaseJunctionModel):
    year_grade_section = models.ForeignKey(YearGradeSection, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("year_grade_section", "student")
        db_table = "year_grade_section_students"
        app_label = "student"
        verbose_name = "year_grade_section_students"


class Parent(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "parents"
        app_label = "student"
        verbose_name = "parents"


class StudentParent(BaseJunctionModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, to_field="id")
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, to_field="id")
    relationship = models.CharField(max_length=50)

    def __str__(self):
        return f"Student: {self.student.first_name} {self.student.last_name}, Parent: {self.parent.first_name} {self.parent.last_name}"

    class Meta:
        unique_together = ("student", "parent")
        db_table = "student_parents"
        app_label = "student"
        verbose_name = "student_parents"


class Attendance(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)
    year_grade_section = models.ForeignKey(
        YearGradeSection, on_delete=models.CASCADE, blank=True
    )

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} {self.date}"

    class Meta:
        unique_together = ("student", "date")
        db_table = "attendances"
        app_label = "student"
