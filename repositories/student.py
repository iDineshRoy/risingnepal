from repositories.base import BaseRepository, BaseJunctionRepository
from domain.aggregates.student import Student, Parent, StudentParent


class StudentRepository(BaseRepository):
    model = Student


class ParentRepository(BaseRepository):
    model = Parent


class StudentParentRepository(BaseJunctionRepository):
    junction_model = StudentParent
    left_model = Student
    right_model = Parent

    def fetch_student_parent(self, **kwargs):
        query = (
            self.junction_model.objects.all(**kwargs)
            .select_related("student", "parent")
            .order_by("-created")
        )
        student_query = self.left_model.objects.all(**kwargs).select_related(
            "student_parents", "parent"
        )
        return student_query.values("student_parents__*", "parent__*", "relationship")
