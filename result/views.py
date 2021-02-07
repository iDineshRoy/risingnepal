from django.shortcuts import render
import xlrd
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def marks_to_grades(marks, full_marks):
    grades = []
    grade_point = []
    for i in (range(len(marks)-2)):
        if type(marks[i]) is not str:
            if (((marks[i])/full_marks[i])>=0.9):
                grades.append("A+")
                grade_point.append(float('4'))
            elif (((marks[i])/full_marks[i])>=0.8 and ((marks[i])/full_marks[i])<0.9):
                grades.append("A")
                grade_point.append(float('3.6'))
            elif (((marks[i])/full_marks[i])>=0.7 and ((marks[i])/full_marks[i])<0.8):
                grades.append("B+")
                grade_point.append(float('3.2'))
            elif (((marks[i])/full_marks[i])>=0.6 and ((marks[i])/full_marks[i])<0.7):
                grades.append("B")
                grade_point.append(float('2.8'))
            elif (((marks[i])/full_marks[i])>=0.5 and ((marks[i])/full_marks[i])<0.6):
                grades.append("C+")
                grade_point.append(float('2.4'))
            elif (((marks[i])/full_marks[i])>=0.4 and ((marks[i])/full_marks[i])<0.5):
                grades.append("C")
                grade_point.append(float('2'))
            elif (((marks[i])/full_marks[i])>=0.3 and ((marks[i])/full_marks[i])<0.4):
                grades.append("D+")
                grade_point.append(float('1.6'))
            elif (((marks[i])/full_marks[i])>=0.2 and ((marks[i])/full_marks[i])<0.3):
                grades.append("D")
                grade_point.append(float('1.2'))
            else:
                grades.append("E")
                grade_point.append(float('.8'))
        else:
            grades.append('AB')
            grade_point.append('AB')
    return grades, grade_point

def homepage(request):
    return render(request, "base.html")

def plustwo(request):
    return render(request, "+2program.html")

def contact(request):
    return render(request, "contact.html")

def termwise(request):
    if request.method == 'POST':
        try:
            year = request.POST['year']
            studentid = int(request.POST['studentid'])
            clas = request.POST['clas']
            exam = request.POST['exam']
            path = os.path.join(BASE_DIR, "static/results/"+year+"/"+exam+".xlsx")
            workbook = xlrd.open_workbook(path)
            worksheet = workbook.sheet_by_name(clas)
            for x in range(worksheet.nrows):
                row_value = worksheet.row_values(x)
                if row_value[0] is not '':
                    print(str(row_value[0]).strip('.0'))
                    if str(row_value[0]).strip('.0')==str(studentid):
                        id=x
                        print("Printing x: "+str(x))
            students_name = worksheet.cell_value(id, 2)
            print(students_name)
            subjects=[]
            marks=[]
            full_marks = []
            for x in range(3, worksheet.ncols):
                subjects.append(worksheet.cell_value(2,x))
                full_marks.append(worksheet.cell_value(3,x))
                marks.append(worksheet.cell_value(id,x))
            grade, grade_point = marks_to_grades(marks, full_marks)
            print(marks)
            print(grade, grade_point)
            try:
                gpa=round((sum(grade_point))/(len(grade_point)), 3)
            except:
                print("Mark missing")
                gpa=""
            try:
                attendance = int(worksheet.cell_value(id, worksheet.ncols-1))
            except:
                attendance = ''
            data = [{'subjects': t[0], 'grade': t[1], 'grade_point':t[2]} for t in zip(subjects, grade, grade_point)]
            return render(request, 'termwise.html', context={ 'students_name': students_name, 'clas':clas, 'marks':marks,   'gpa':gpa, 'attendance':attendance, 'data':data })
        except:
            pass
    return render(request, 'termwise.html')

def get_result(request):
    name = ''
    new_path = os.path.join(BASE_DIR, "static/results")
    years = [name for name in os.listdir(new_path)]
    return render(request, 'get_result.html', context={'years': years})