from django.contrib import admin

from domain.aggregates.student import (
    Student,
    Parent,
    StudentParent,
)
from .models import BillModel, PaymentModel


admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(StudentParent)
admin.site.register(BillModel)
admin.site.register(PaymentModel)
