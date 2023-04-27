from rest_framework import viewsets
from .serializers import StudentSerializer
from domain.aggregates.student import Student
from repositories.student import StudentRepository


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    repository_class = StudentRepository

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.repository_class(self.request.user).filter(queryset)

    def perform_create(self, serializer):
        repository = self.repository_class(self.request.user)
        serializer.save(repository=repository)
