from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from student.views import (
    StudentView,
    StudentListView,
    ParentView,
    StudentParentView,
    YearGradeSectionView,
    YearGradeSectionStudentView,
)

from repositories.student import StudentRepository
from domain.aggregates import Student, Bill
from django.urls import path, reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from repositories.forms import FeeForm
from student.forms import StudentForm

from application.base import BaseView

# ---------------------------------------------------- #


sv = StudentView()
pv = ParentView()
spv = StudentParentView()
ygs = YearGradeSectionView()
ygss = YearGradeSectionStudentView()
urlpatterns = (
    [
        path("list_students/", StudentListView.as_view(), name="list_students"),
    ]
    + sv.url_patterns()
    + pv.url_patterns()
    + spv.url_patterns()
    + ygs.url_patterns()
    + ygss.url_patterns()
)
