from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError

from domain.aggregates.base import BaseModel, BaseJunctionModel
from domain.aggregates.student import Student
from decimal import Decimal


class Fee(BaseModel):
    FEE_CHOICES = (
        ("Admission Fee", "Admission Fee"),
        ("Monthly Fee", "Monthly Fee"),
        ("Exam Fee", "Exam Fee"),
        ("Sarashwati Puja", "Sarashwati Puja"),
        ("Tie Long", "Tie Long"),
        ("Tie Short", "Tie Short"),
    )

    fee_type = models.CharField(max_length=40, choices=FEE_CHOICES)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    year_grade_section = models.ManyToManyField(
        "YearGradeSection", through="YearGradeSectionStudent"
    )

    def __str__(self) -> str:
        return f"{self.fee_type}: {self.amount}"

    class Meta:
        db_table = "fees"
        app_label = "student"


class FeeStudent(BaseJunctionModel):
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal(0))

    def __str__(self) -> str:
        return (
            f"{self.student.first_name} {self.student.last_name}: {self.fee.fee_type}"
        )

    def save(self, *args, **kwargs):
        if self.fee.year_grade_section != self.student.year_grade_section:
            raise ValidationError(
                "Student and Fee must correlate to the same year, class, section."
            )

    class Meta:
        db_table = "fee_students"
        app_label = "student"


class Bill(BaseModel):
    STATUS_CHOICES = (
        ("Due", "Due"),
        ("Unpaid", "Unpaid"),
        ("Partially Paid", "Partially Paid"),
        ("Void", "Void"),
        ("Paid", "Paid"),
    )
    fee_student = models.ForeignKey(FeeStudent, on_delete=models.CASCADE, blank=True)
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE, blank=True)
    due_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)

    def __str__(self) -> str:
        return f"{self.due_date} {self.fee_student.student.first_name} {self.fee_student.student.last_name}: {self.fee.fee_type}"

    def save(self, *args, **kwargs):
        if self.fee.year_grade_section != self.fee_student.student.year_grade_section:
            raise ValidationError(
                "Student and Fee must correlate to the same year, class, section."
            )

    class Meta:
        db_table = "bills"
        app_label = "student"


class Receipt(BaseModel):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
