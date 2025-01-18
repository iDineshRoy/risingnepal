from rest_framework.serializers import ModelSerializer
from .student import Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
