from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from student.views import (
    StudentView,
    # StudentListView,
    ParentView,
    StudentParentView,
    YearGradeSectionView,
    YearGradeSectionStudentView,
)

from repositories.student import StudentRepository
from domain.aggregates import Student, Bill
from django.urls import path, reverse_lazy


from application.views.bill import FeeView, FeeStudentView, BillView
from repositories import FeeAutocompleteView, StudentParentAutocompleteView


# ---------------------------------------------------- #


fv = FeeView()
fsv = FeeStudentView()
bv = BillView()

urlpatterns = (
    [
        path("select2/", include("django_select2.urls")),
    ]
    + fv.url_patterns()
    + fsv.url_patterns()
    + bv.url_patterns()
)
