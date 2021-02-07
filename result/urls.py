from django.urls import path, include
from .views import homepage, plustwo, contact, termwise, get_result
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',homepage, name='home'),
    path('plustwo',plustwo, name='plustwo'),
    path('contact',contact, name='contact'),
    path('termwise',termwise, name='termwise'),
    path('result',get_result, name='get_term'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)