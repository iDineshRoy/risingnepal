# models.py

from django.db import models
from domain.models import Student


class Bill(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    issue_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(
        max_length=20, choices=[("unpaid", "Unpaid"), ("paid", "Paid")]
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Bill for {self.student} ({self.amount})"
