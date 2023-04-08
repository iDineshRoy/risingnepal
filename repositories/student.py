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
