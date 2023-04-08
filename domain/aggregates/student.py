from django.db import models

from domain.aggregates.base import BaseModel, BaseJunctionModel


class StudentModel(BaseModel):
    # This contains the personal details about the students
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(blank=True, null=True)
    roll_number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    admitted_on = models.DateField(blank=True, null=True)
    year = models.ManyToManyField("YearModel", through="YearStudentModel", blank=True)
    year_grade = models.ManyToManyField(
        "YearGradeModel", through="YearGradeStudentModel", blank=True
    )
    year_grade_section = models.ManyToManyField(
        "YearGradeSectionModel", through="YearGradeSectionStudentModel", blank=True
    )

    class Meta:
        db_table = "students"
        app_label = "student"


class YearModel(BaseModel):
    # This is for the academic year
    year = models.IntegerField()
    year_ad = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    grades = models.ManyToManyField("GradeModel", through="YearGradeModel")

    class Meta:
        db_table = "years"
        app_label = "student"


class GradeModel(BaseModel):
    # This is for the class. Domain word is class, but we use grade
    # For Python reasons
    grade = models.CharField(max_length=20)
    grade_num = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    years = models.ManyToManyField("YearModel", through="YearGradeModel")

    class Meta:
        db_table = "grades"
        app_label = "student"


class SectionModel(BaseModel):
    # This is for the class. Domain word is class, but we use grade
    # For Python reasons
    section = models.CharField(max_length=20)
    section_num = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = "sections"
        app_label = "student"


class YearGradeModel(BaseJunctionModel):
    year = models.ForeignKey(YearModel, on_delete=models.CASCADE)
    grade = models.ForeignKey(GradeModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("year", "grade")
        db_table = "year_grades"
        app_label = "student"


class YearGradeStudentModel(BaseJunctionModel):
    year_grade = models.ForeignKey(YearGradeModel, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("year_grade", "student")
        db_table = "year_grade_students"
        app_label = "student"


class GradeSectionModel(BaseJunctionModel):
    grade = models.ForeignKey(GradeModel, on_delete=models.CASCADE)
    section = models.ForeignKey(SectionModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("grade", "section")
        db_table = "grade_sections"
        app_label = "student"


class YearGradeSectionModel(BaseJunctionModel):
    year_grade = models.ForeignKey(YearGradeModel, on_delete=models.CASCADE)
    section = models.ForeignKey(SectionModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("year_grade", "section")
        db_table = "year_grade_sections"
        app_label = "student"


class YearGradeSectionStudentModel(BaseJunctionModel):
    year_grade_section = models.ForeignKey(
        YearGradeSectionModel, on_delete=models.CASCADE
    )
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("year_grade_section", "student")
        db_table = "year_grade_section_students"
        app_label = "student"


class YearStudentModel(BaseJunctionModel):
    # This is the junction table that contains the number of
    # all the students in a year

    year = models.ForeignKey(YearModel, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("year", "student")
        db_table = "year_students"
        app_label = "student"


class ParentModel(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = "parents"
        app_label = "student"


class StudentParentModel(BaseJunctionModel):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE, to_field="id")
    parent = models.ForeignKey(ParentModel, on_delete=models.CASCADE, to_field="id")
    relationship = models.CharField(max_length=50)

    class Meta:
        unique_together = ("student", "parent")
        db_table = "student_parents"
        app_label = "student"


# class Student(Entity):
#     _first_name: str
#     _last_name: str
#     _roll_number: int | None
#     _grade: str | None
#     _dob: date | None
#     _address: str | None
#     _phone_number: str | None

#     def __init__(
#         self,
#         id: int,
#         first_name: str,
#         last_name: str,
#         roll_number: int | None,
#         grade: str,
#         dob: date | None,
#         address: str | None,
#         phone_number: str | None,
#     ):
#         super().__init__(id)
#         self._first_name = first_name
#         self._last_name = last_name
#         self._roll_number = roll_number
#         self._grade = grade
#         self._dob = dob
#         self._address = address
#         self._phone_number = phone_number


# class Parent(Entity):
#     _first_name: str
#     _last_name: str
#     _address: str
#     _phone_number: str
#     _email: str

#     def __init__(
#         self,
#         id: int,
#         first_name: str,
#         last_name: str,
#         address: str,
#         phone_number: str,
#         email: str,
#     ):
#         super().__init__(id)
#         self._first_name = first_name
#         self._last_name = last_name
#         self._phone_number = phone_number
#         self._email = email
#         self._address = address


# class StudentParent:
#     _student_id: int
#     _parent_id: int
#     _relationship: str

#     def __init__(self, student_id: int, parent_id: int, relationship: str):
#         super().__init__()
#         self._student_id = student_id
#         self._parent_id = parent_id
#         self._relationship = relationship
