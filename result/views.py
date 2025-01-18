from django.shortcuts import get_object_or_404, render, get_list_or_404
import xlrd
import os
from os import listdir, name
from os.path import isfile, join

from pathlib import Path
from blog.models import Post
from django.http import JsonResponse

BASE_DIR = Path(__file__).resolve().parent.parent


def marks_to_grades(marks, full_marks):
    grades = []
    grade_point = []
    for i in range(len(marks) - 2):
        if type(marks[i]) is not str:
            if ((marks[i]) / full_marks[i]) >= 0.9:
                grades.append("A+")
                grade_point.append(float("4"))
            elif ((marks[i]) / full_marks[i]) >= 0.8 and (
                (marks[i]) / full_marks[i]
            ) < 0.9:
                grades.append("A")
                grade_point.append(float("3.6"))
            elif ((marks[i]) / full_marks[i]) >= 0.7 and (
                (marks[i]) / full_marks[i]
            ) < 0.8:
                grades.append("B+")
                grade_point.append(float("3.2"))
            elif ((marks[i]) / full_marks[i]) >= 0.6 and (
                (marks[i]) / full_marks[i]
            ) < 0.7:
                grades.append("B")
                grade_point.append(float("2.8"))
            elif ((marks[i]) / full_marks[i]) >= 0.5 and (
                (marks[i]) / full_marks[i]
            ) < 0.6:
                grades.append("C+")
                grade_point.append(float("2.4"))
            elif ((marks[i]) / full_marks[i]) >= 0.4 and (
                (marks[i]) / full_marks[i]
            ) < 0.5:
                grades.append("C")
                grade_point.append(float("2"))
            elif ((marks[i]) / full_marks[i]) >= 0.3 and (
                (marks[i]) / full_marks[i]
            ) < 0.4:
                grades.append("D+")
                grade_point.append(float("1.6"))
            elif ((marks[i]) / full_marks[i]) >= 0.2 and (
                (marks[i]) / full_marks[i]
            ) < 0.3:
                grades.append("D")
                grade_point.append(float("1.2"))
            else:
                grades.append("E")
                grade_point.append(float(".8"))
        else:
            grades.append("AB")
            grade_point.append("AB")
    return grades, grade_point


def homepage(request):
    context = {}
    try:
        posts = get_list_or_404(
            Post.objects.filter(status="Published").order_by("-id")[:3]
        )
        context["posts"] = posts
    except:
        context["posts"] = ""
    return render(request, "base.html", context)


def plustwo(request):
    return render(request, "+2program.html")


def contact(request):
    return render(request, "contact.html")


def termwise(request):
    if request.method == "POST":
        try:
            year = request.POST["year"]
            studentid: str = request.POST["studentid"]
            clas = request.POST["clas"]
            exam = request.POST["exam"]
            path = os.path.join(
                BASE_DIR, "static/results/" + year + "/" + exam + ".xlsx"
            )
            workbook = xlrd.open_workbook(path)
            worksheet = workbook.sheet_by_name(clas)
            for x in range(worksheet.nrows):
                row_value = worksheet.row_values(x)
                if row_value[0] != "":
                    # print(str(row_value[0]).strip('.0'))
                    # if str(row_value[0]).strip('.0')==str(studentid):

                    if str(row_value[0]) == (str(studentid)):
                        id = x
                        print("Printing x: " + str(x))
            students_name = worksheet.cell_value(id, 2)
            print(students_name)
            subjects = []
            marks = []
            full_marks = []
            for x in range(3, worksheet.ncols):
                subjects.append(worksheet.cell_value(2, x))
                full_marks.append(worksheet.cell_value(3, x))
                marks.append(worksheet.cell_value(id, x))
            grade, grade_point = marks_to_grades(marks, full_marks)
            print(marks)
            print(grade, grade_point)
            try:
                gpa = round((sum(grade_point)) / (len(grade_point)), 3)
            except:
                print("Mark missing")
                gpa = ""
            try:
                attendance = int(worksheet.cell_value(id, worksheet.ncols - 1))
            except:
                attendance = ""
            data = [
                {"subjects": t[0], "grade": t[1], "grade_point": t[2]}
                for t in zip(subjects, grade, grade_point)
            ]
            return render(
                request,
                "termwise.html",
                context={
                    "students_name": students_name,
                    "clas": clas,
                    "marks": marks,
                    "gpa": gpa,
                    "attendance": attendance,
                    "data": data,
                },
            )
        except:
            pass
    return render(request, "termwise.html")


from django import middleware as md


def json_termwise(request):
    if request.method == "GET":
        try:
            year = request.GET["year"]
            studentid = int(request.GET["studentid"])
            clas = request.GET["clas"]
            exam = request.GET["exam"]
            print(exam)
            path = os.path.join(
                BASE_DIR, "static/results/" + year + "/" + exam + ".xlsx"
            )
            workbook = xlrd.open_workbook(path)
            worksheet = workbook.sheet_by_name(clas)
            for x in range(worksheet.nrows):
                row_value = worksheet.row_values(x)
                if row_value[0] != "":
                    print(str(row_value[0]).strip(".0"))
                    if str(row_value[0]).strip(".0") == str(studentid):
                        id = x
                        print("Printing x: " + str(x))
            students_name = worksheet.cell_value(id, 2)
            print(students_name)
            subjects = []
            marks = []
            full_marks = []
            for x in range(3, worksheet.ncols):
                subjects.append(worksheet.cell_value(2, x))
                full_marks.append(worksheet.cell_value(3, x))
                marks.append(worksheet.cell_value(id, x))
            grade, grade_point = marks_to_grades(marks, full_marks)
            print(marks)
            print(grade, grade_point)
            try:
                gpa = round((sum(grade_point)) / (len(grade_point)), 3)
            except:
                print("Mark missing")
                gpa = ""
            try:
                attendance = int(worksheet.cell_value(id, worksheet.ncols - 1))
            except:
                attendance = ""
            data = [
                {"subjects": t[0], "grade": t[1], "grade_point": t[2]}
                for t in zip(subjects, grade, grade_point)
            ]
            context = {
                "students_name": students_name,
                "clas": clas,
                "marks": marks,
                "gpa": gpa,
                "attendance": attendance,
                "data": data,
            }
            response = JsonResponse(context)
        except:
            response = JsonResponse({"error": "some error occured"})
    return response


def get_result(request):
    context = {}
    new_path = os.path.join(BASE_DIR, "static/results")
    years = [
        name
        for name in os.listdir(new_path)
        if os.path.isdir(os.path.join(new_path, name))
    ]
    context["years"] = years
    classes = set()
    terms_list = set()
    for year in years:
        new_path = os.path.join(BASE_DIR, "static/results/" + year)
        terms = [name for name in os.listdir(new_path)]
        terms_list.update([name.replace(".xlsx", "") for name in os.listdir(new_path)])
        for term in terms:
            path = os.path.join(BASE_DIR, "static/results/" + year + "/" + term)
            workbook = xlrd.open_workbook(path, on_demand=True)
            classes.update(workbook.sheet_names())
    # context['classes']=sorted(list(classes))
    context["terms"] = sorted(list(terms_list))
    return render(request, "get_result.html", context)


def workbook_data(path, clas, studentid, ep):
    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_name(clas)
    for x in range(worksheet.nrows):
        row_value = worksheet.row_values(x)
        if row_value[0] != "":
            # print(str(row_value[0]).strip('.0'))
            if str(row_value[0]).strip(".0") == str(studentid):
                id = x
                print("Printing x: " + str(x))
    students_name = worksheet.cell_value(id, 2)
    print(students_name)
    subjects = []
    marks = []
    full_marks = []
    for x in range(3, worksheet.ncols):
        subjects.append(worksheet.cell_value(2, x))
        full_marks.append(worksheet.cell_value(3, x))
        try:
            marks.append(
                float(worksheet.cell_value(id, x)) * ep
            )  # multiplied by effective percentage
        except:
            marks.append(0)

    try:
        attendance = int(worksheet.cell_value(id, worksheet.ncols - 1))
    except:
        attendance = 0
    # data = [{'subject': t[0], 'grade': t[1], 'grade_point':t[2]} for t in zip(subjects, grade, grade_point)]
    return subjects, marks, attendance, full_marks, students_name


def annual_result(request):
    if request.method == "POST":
        try:
            year = request.POST["year"]
            studentid = int(request.POST["studentid"])
            clas = request.POST["clas"]

            mypath = os.path.join(BASE_DIR, "static/results/" + year + "/")
            all_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

            exams_filename = [os.path.splitext(name)[0] for name in all_files]
            count = 0
            marks = []
            attendance = 0
            for exam in all_files:
                print(exam)
                path = os.path.join(BASE_DIR, "static/results/" + year + "/" + exam)
                subs, m, atten, full_marks, students_name = workbook_data(
                    path, clas, studentid, (1 / len(all_files))
                )
                marks.append(list(m))
                attendance = attendance + atten
                # print(sub, marks)
                count = count + 1
            num = len(marks)  # how many term marks are here
            if num == 1:
                new_marks = marks[0]
            elif num == 2:
                new_marks = [x + y for (x, y) in zip(marks[0], marks[1])]
            elif num == 3:
                new_marks = [
                    x + y + z for (x, y, z) in zip(marks[0], marks[1], marks[2])
                ]
            elif num == 4:
                new_marks = [
                    x + y + z + aa
                    for (x, y, z, aa) in zip(marks[0], marks[1], marks[2], marks[3])
                ]
            else:
                print("Some error occured")

            grade, grade_point = marks_to_grades(new_marks, full_marks)
            print(subs, marks, grade, grade_point)

            try:
                gpa = round((sum(grade_point)) / (len(grade_point)), 3)
            except:
                print("Mark missing")
                gpa = ""
            # attendance = '234' #just for now
            data = [
                {"subjects": t[0], "grade": t[1], "grade_point": t[2]}
                for t in zip(subs, grade, grade_point)
            ]
            return render(
                request,
                "termwise.html",
                context={
                    "students_name": students_name,
                    "clas": clas,
                    "marks": marks,
                    "gpa": gpa,
                    "attendance": attendance,
                    "data": data,
                    "exams_filename": exams_filename,
                },
            )
        except:
            pass
    return render(request, "termwise.html")


def get_annual(request):
    context = {}
    new_path = os.path.join(BASE_DIR, "static/results")
    years = [
        name
        for name in os.listdir(new_path)
        if os.path.isdir(os.path.join(new_path, name))
    ]
    context["years"] = years
    classes = set()
    for year in years:
        new_path = os.path.join(BASE_DIR, "static/results/" + year)
        terms = [name for name in os.listdir(new_path)]
        for term in terms:
            path = os.path.join(BASE_DIR, "static/results/" + year + "/" + term)
            workbook = xlrd.open_workbook(path, on_demand=True)
            classes.update(workbook.sheet_names())
    context["classes"] = sorted(list(classes))
    return render(request, "get_annual.html", context)


def get_classes(request):
    print("Now this funtion is working")
    if request.is_ajax():
        year = request.POST.get("get-year")
    else:
        year = ""
    context = {}
    classes = set()
    terms_list = set()
    new_path = os.path.join(BASE_DIR, "static/results/" + year)
    terms = [
        name
        for name in os.listdir(new_path)
        if os.path.isdir(os.path.join(new_path, name))
    ]
    terms_list.update([name.replace(".xlsx", "") for name in os.listdir(new_path)])
    for term in terms:
        path = os.path.join(BASE_DIR, "static/results/" + year + "/" + term)
        workbook = xlrd.open_workbook(path, on_demand=True)
        classes.update(workbook.sheet_names())
    context["classes"] = sorted(list(classes))
    print(context["classes"])
    context["terms"] = sorted(list(terms_list))
    return render(request, "getclasses.html", context)
