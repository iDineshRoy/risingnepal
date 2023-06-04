from domain.aggregates import FeeStudent, StudentParent
from typing import Any
from django.db import models


class FeeAutocompleteView:
    name = "fee_studentauto"
    multiselect = True

    class Meta:
        model = FeeStudent


class StudentParentAutocompleteView:
    name = "student_parentauto"
    multiselect = True
    custom_strings = {
        "no_results": "no results text",
        "more_results": ("More results text"),
    }

    class Meta:
        model = StudentParent
