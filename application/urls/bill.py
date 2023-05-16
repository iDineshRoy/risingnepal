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


from application.views.bill import FeeView, FeeStudentView

# ---------------------------------------------------- #


fv = FeeView()
fsv = FeeStudentView()
urlpatterns = [] + fv.url_patterns() + fsv.url_patterns()
