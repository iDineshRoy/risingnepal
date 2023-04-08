from django.contrib import admin

from domain.aggregates.student import (
    StudentModel,
    ParentModel,
    StudentParentModel,
)
from .models import BillModel, PaymentModel


admin.site.register(StudentModel)
admin.site.register(ParentModel)
admin.site.register(StudentParentModel)
admin.site.register(BillModel)
admin.site.register(PaymentModel)
