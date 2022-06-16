from django.urls import path
from .views import show_file, show_files_list, view_year, show_terms

app_name='qbank'
urlpatterns = [
    path(r'open/<str:year>/<str:term>/<str:file>/', show_file, name='open_docx'),
    path(r'question/<year>/<term>/', show_files_list, name='show_questions'),
    path(r'year/', view_year, name='show_year'),
    path(r'term/<str:year>/', show_terms, name='show_terms'),
]