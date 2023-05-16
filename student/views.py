from typing import Any, Dict
import nepali_datetime

from django.shortcuts import render
from django.db.models import F
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from domain.aggregates import (
    Student,
    StudentParent,
    Parent,
    Attendance,
    YearGradeSection,
    YearGradeSectionStudent,
)

from repositories.student import (
    StudentParentRepository,
    StudentRepository,
    ParentRepository,
)
from .forms import StudentForm, ParentForm, StudentParentForm
from repositories.forms import YearGradeSectionForm, YearGradeSectionStudentForm

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from application.base import BaseView


# ---------------------------------------------------- #


class StudentView(BaseView):
    model = Student
    form_class = StudentForm
    context_object_name = "students"
    student_parents = StudentParent.objects.all()
    yeargradesectionstudent = YearGradeSectionStudent.objects.all()
    more_context = {
        "student_parents": student_parents,
        "yeargradesectionstudent": yeargradesectionstudent,
    }
    template_name = "list_student.html"


class ParentView(BaseView):
    model = Parent
    form_class = ParentForm
    context_object_name = "students"
    template_name = "list_parent.html"


class StudentParentView(BaseView):
    model = StudentParent
    form_class = StudentParentForm
    context_object_name = "students"
    template_name = "list_studentparent.html"


class YearGradeSectionView(BaseView):
    model = YearGradeSection
    form_class = YearGradeSectionForm
    context_object_name = "objects"
    template_name = "list_yeargradesection.html"


class YearGradeSectionStudentView(BaseView):
    model = YearGradeSectionStudent
    form_class = YearGradeSectionStudentForm
    context_object_name = "objects"
    template_name = "list_yeargradesectionstudent.html"


# class StudentListView(ListView):
#     model = Student
#     template_name = "list_students.html"
#     context_object_name = "students"
#     paginate_by = 10
#     ordering = ["-modified", "-created"]

#     def get_queryset(self):
#         students = StudentRepository()
#         students = students.get_all()
#         return students

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         student_parents = StudentParent.objects.prefetch_related("student").all()
#         attendance = Attendance.objects.prefetch_related("student").all()
#         yeargradesectionstudent = YearGradeSectionStudent.objects.all()
#         context["attendances"] = attendance
#         context["student_parents"] = student_parents
#         context["yeargradesectionstudent"] = yeargradesectionstudent
#         return context


class StudentDetailView(DetailView):
    model = Student
    template_name = "student_detail.html"
    context_object_name = "Student"


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    template_name = "student_create.html"
    form_class = StudentForm
    success_url = reverse_lazy("list_student")

    def form_valid(self, form):
        return super().form_valid(form)


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = "student_update.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# class StudentDeleteView(LoginRequiredMixin, DeleteView):
#     model = Student
#     template_name = 'student_delete.html'
#     success_url = reverse_lazy('Student_list')

#     def get_object(self, queryset=None):
#         obj = super().get_object(queryset=queryset)
#         if not obj.author == self.request.user:
#             raise Http404
#         return obj


class StudentParentListView(ListView):
    model = StudentParent
    template_name = "student_parent_list.html"
    context_object_name = "student_parents"
    paginate_by = 15


class StudentParentDetailView(DetailView):
    model = StudentParent
    template_name = "student_detail.html"
    context_object_name = "students"


class StudentParentCreateView(LoginRequiredMixin, CreateView):
    model = StudentParent
    form_class = StudentParentForm
    template_name = "create_student_parent.html"
    success_url = reverse_lazy("list_student")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["student_form"] = StudentForm()
        context["parent_form"] = ParentForm()
        return context

    def form_valid(self, form):
        student_form = StudentForm(self.request.POST)
        parent_form = ParentForm(self.request.POST)
        if student_form.is_valid() and parent_form.is_valid():
            student = student_form.save()
            parent = parent_form.save()
            student_parent = form.save(commit=False)
            student_parent.student = student
            student_parent.parent = parent
            student_parent.relationship = form.cleaned_data["relationship"]
            student_parent.save()
            return super().form_valid(form)
        context = self.get_context_data(
            form=form, student_form=student_form, parent_form=parent_form
        )
        return self.render_to_response(context)


class StudentParentAssignView(LoginRequiredMixin, CreateView):
    model = StudentParent
    template_name = "student_create.html"
    fields = ["student", "parent", "relationship"]
    success_url = reverse_lazy("list_student")

    def form_valid(self, form):
        return super().form_valid(form)


class StudentParentUpdateView(LoginRequiredMixin, UpdateView):
    model = StudentParent
    template_name = "student_update.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ParentCreateView(LoginRequiredMixin, CreateView):
    model = Parent
    template_name = "student_create.html"
    fields = ["first_name", "last_name", "phone_number", "email", "address"]
    success_url = reverse_lazy("student_list")

    def form_valid(self, form):
        return super().form_valid(form)


class ParentListView(LoginRequiredMixin, CreateView):
    model = Parent
    template_name = "list_student.html"
    context_object_name = "parents"
    paginate_by = 10
    ordering = ["-modified", "-created"]

    def get_queryset(self):
        students = ParentRepository()
        students = students.get_all()
        return students

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student_parents = StudentParent.objects.prefetch_related("student").all()
        attendance = Attendance.objects.prefetch_related("student").all()
        context["attendances"] = attendance
        context["student_parents"] = student_parents
        return context
