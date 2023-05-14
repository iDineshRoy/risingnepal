from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("result.urls")),
    path("blog/", include("blog.urls")),
    path("bill/", include("application.urls.bill")),
    # path("accounts/", include("accounts.urls")),
    path("student/", include("student.urls")),
    path("users/", include("users.urls")),
    path(r"model_questions/", include(("qbank.urls", "qbank"), namespace="qbank")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
