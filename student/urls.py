from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from student.views import (
    StudentCreateView,
    StudentListView,
    StudentParentCreateView,
    StudentParentAssignView,
    StudentParentListView,
    ParentCreateView,
)

from repositories.student import StudentRepository
from domain.aggregates.student import StudentModel
from django.urls import path


urlpatterns = [
    # path("/", include(student_router), name="student-routes"),
    path("list_student/", StudentListView.as_view(), name="list_student"),
    path("create_student/", StudentCreateView.as_view(), name="create_student"),
    path(
        "assign_student_parent/",
        StudentParentAssignView.as_view(),
        name="assign_student_parent",
    ),
    path(
        "list_student_parent/",
        StudentParentListView.as_view(),
        name="list_student_parent",
    ),
    path("create_parent/", ParentCreateView.as_view(), name="create_parent"),
    path(
        "create_student_parent/",
        StudentParentCreateView.as_view(),
        name="create_student_parent",
    ),
]
