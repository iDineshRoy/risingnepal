from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from student.views import test

urlpatterns = [
    path("", test, name="test"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
