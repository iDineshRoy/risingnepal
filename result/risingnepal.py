import xlrd
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

path = os.path.join(BASE_DIR, "static/results/2077/First Term.xlsx")

workbook = xlrd.open_workbook(path)
print(workbook.sheet_names())
class_name = input("Please enter the class: ")
worksheet = workbook.sheet_by_name(class_name)

student={}
student['roll_no']=[]
student['name']=[]
for x in range(6, worksheet.nrows):
    student['roll_no'].append(int(worksheet.cell_value(x,0)))
    student['name'].append(worksheet.cell_value(x,1))

subjects=[]
marks=[]
roll_no=int(input("Enter roll no.:"))

students_name = worksheet.cell_value(roll_no+5, 1)
full_marks = []
for x in range(2, worksheet.ncols):
    subjects.append(worksheet.cell_value(2,x))
    full_marks.append(worksheet.cell_value(3,x))
    marks.append(worksheet.cell_value(roll_no+5,x))

print(full_marks)
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

print("Marks objtained by: "+students_name)
# print(student)
print(subjects)
print(marks)
grade, grade_point = marks_to_grades(marks, full_marks)
try:
    gpa=(sum(grade_point))/(len(grade_point))
    print(round(gpa,3))
except:
    print("Mark missing")
    gpa=""
try:
    attendance = print(int(worksheet.cell_value(roll_no+5, worksheet.ncols-1)))
except:
    pass
print(marks_to_grades(marks, full_marks))