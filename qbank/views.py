from django.shortcuts import render
import os
from pathlib import Path
import mammoth

BASE_DIR = Path(__file__).resolve().parent.parent

def show_file(request, year, term, file):
    context = {}
    try:
        path = "static/Questions/"+year+'/'+term.replace("%20", " ")+'/'+file.replace("%20", " ")
        new_path = os.path.join(BASE_DIR, path)
        with open(new_path.replace("%20", " "), "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html = result.value # The generated HTML
            messages = result.messages # Any messages, such as warnings during conversion
        context['question']=html
        context['year']=year
        context['term']=term.replace("%20", " ")
        context['file']=file.replace("%20", " ")
        return render(request, 'show_file.html', context)
    except:
        context['messsage'] = "Sorry! Can't open the question.<br>Please, contact: info@vpit.com.np if the issue persists."
        return render(request, 'message.html', context)

def show_files_list(request, year, term):
    context = {}
    try:
        path = "static/Questions/"+year+'/'+term.replace("%20", " ")
        new_path = os.path.join(BASE_DIR, path)
        print(new_path)
        context['allfiles'] = os.listdir(os.path.abspath(new_path))
        context['year'] = year
        context['term'] = term.replace("%20", " ")
        return render(request, 'show_files_list.html', context)
    except:
        context['messsage'] = "Sorry! Some error occured.<br>Please, contact: info@vpit.com.np if the issue persists."
        return render(request, 'message.html', context)

def view_year(request):
    context = {}
    path = "static/Questions/"
    new_path = os.path.join(BASE_DIR, path)
    context['years'] = sorted(os.listdir(new_path))
    context['path'] = path
    return render(request, 'show_year.html', context)

def show_terms(request, year):
    context = {}
    try:
        path = "static/Questions/"+year+'/'
        new_path = os.path.join(BASE_DIR, path)
        context['terms'] = os.listdir(new_path)
        print(context['terms'])
        context['year'] = year
        return render(request, 'show_terms.html', context)
    except:
        context['messsage'] = "Sorry! Some error occured.<br>Please, contact: info@vpit.com.np if the issue persists."
        return render(request, 'message.html', context)