from django.shortcuts import render
from repositories.student import StudentParentRepository
from django.http import HttpResponse

# Create your views here.


def test(request):
    repo = StudentParentRepository()
    obj = repo.create(
        left_data={"first_name": "Samir", "last_name": "Wagle"},
        right_data={"first_name": "Padam", "last_name": "Wagle"},
    )
    return HttpResponse("Howdy")
