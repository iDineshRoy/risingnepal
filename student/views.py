from typing import Any, Dict

from django.shortcuts import render
from repositories.student import StudentParentRepository, StudentRepository
from django.http import HttpResponse
from django.views.generic.base import TemplateView


from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from domain.aggregates.student import StudentModel, StudentParentModel, ParentModel


from .forms import StudentForm, ParentForm, StudentParentForm

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class StudentListView(ListView):
    model = StudentModel
    template_name = "list_student.html"
    context_object_name = "students"
    paginate_by = 10
    ordering = ["-modified", "-created"]

    def get_queryset(self):
        student = StudentRepository()
        return student.get_all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # retrieve all books, and prefetch the related authors
        student_parents = StudentParentModel.objects.prefetch_related("student").all()
        context["student_parents"] = student_parents
        return context


class StudentDetailView(DetailView):
    model = StudentModel
    template_name = "student_detail.html"
    context_object_name = "Student"


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = StudentModel
    template_name = "student_create.html"
    form_class = StudentForm
    success_url = reverse_lazy("list_student")

    def form_valid(self, form):
        return super().form_valid(form)


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = StudentModel
    template_name = "student_update.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# class StudentDeleteView(LoginRequiredMixin, DeleteView):
#     model = StudentModel
#     template_name = 'student_delete.html'
#     success_url = reverse_lazy('Student_list')

#     def get_object(self, queryset=None):
#         obj = super().get_object(queryset=queryset)
#         if not obj.author == self.request.user:
#             raise Http404
#         return obj


class StudentParentListView(ListView):
    model = StudentParentModel
    template_name = "student_parent_list.html"
    context_object_name = "student_parents"
    paginate_by = 15


class StudentParentDetailView(DetailView):
    model = StudentParentModel
    template_name = "student_detail.html"
    context_object_name = "students"


class StudentParentCreateView(LoginRequiredMixin, CreateView):
    model = StudentParentModel
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
    model = StudentParentModel
    template_name = "student_create.html"
    fields = ["student", "parent", "relationship"]
    success_url = reverse_lazy("list_student")

    def form_valid(self, form):
        return super().form_valid(form)


class StudentParentUpdateView(LoginRequiredMixin, UpdateView):
    model = StudentParentModel
    template_name = "student_update.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ParentCreateView(LoginRequiredMixin, CreateView):
    model = ParentModel
    template_name = "student_create.html"
    fields = ["first_name", "last_name", "phone_number", "email", "address"]
    success_url = reverse_lazy("student_list")

    def form_valid(self, form):
        return super().form_valid(form)