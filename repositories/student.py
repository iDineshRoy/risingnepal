from repositories.base import BaseRepository, BaseJunctionRepository
from domain.aggregates.student import StudentModel, ParentModel, StudentParentModel


class StudentRepository(BaseRepository):
    model = StudentModel


class ParentRepository(BaseRepository):
    model = ParentModel


class StudentParentRepository(BaseJunctionRepository):
    junction_model = StudentParentModel
    left_model = StudentModel
    right_model = ParentModel

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
