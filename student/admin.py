from django.contrib import admin

from domain.aggregates.student import (
    Student,
    Parent,
    StudentParent,
)
from domain.aggregates import Fee, FeeStudent, Bill

# from .models import BillModel, PaymentModel


admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(StudentParent)
admin.site.register(Fee)
admin.site.register(FeeStudent)
admin.site.register(Bill)
