from django.db import models

from domain.aggregates.base import BaseModel, BaseJunctionModel


class FeeTypeModel(models.Model):
    STUDENT_FEES = "STUDENT_FEES"
    ADMISSION_FEE = "ADMISSION_FEE"
    EXAM_FEE = "EXAM_FEE"
    UNIFORM_FEE = "UNIFORM_FEE"
    OTHER_FEE = "OTHER_FEE"
    BILL_TYPE_CHOICES = [
        (STUDENT_FEES, "Student Fees"),
        (ADMISSION_FEE, "Admission Fee"),
        (EXAM_FEE, "Exam Fee"),
        (UNIFORM_FEE, "Uniform Fee"),
        (OTHER_FEE, "Other Fee"),
    ]
    id = models.BigIntegerField(primary_key=True)
    fee_type = models.CharField(max_length=20, choices=BILL_TYPE_CHOICES)
    amount = models.FloatField()
    bills = models.ManyToManyField("BillModel", through="BillFeeTypeModel")

    class Meta:
        db_table = "fee_type"


class BillModel(BaseModel):
    # Bill model will have multiple fee types
    due_date = models.DateField()
    paid = models.BooleanField(default=False)
    partial_amount = models.FloatField(default=0.0)
    fee_types = models.ManyToManyField("FeeTypeModel", through="BillFeeTypeModel")

    class Meta:
        db_table = "bill"


class BillFeeTypeModel(BaseJunctionModel):
    left = models.ForeignKey(BillModel, on_delete=models.CASCADE)
    right = models.ForeignKey(FeeTypeModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("left", "right")


class PaymentModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    bill = models.ForeignKey(BillModel, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_date = models.DateField()

    class Meta:
        db_table = "payments"
