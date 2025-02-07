from django.urls import path, include
from .views import (
    get_classes,
    homepage,
    plustwo,
    contact,
    termwise,
    get_result,
    json_termwise,
    annual_result,
    get_annual,
)
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from rest_framework import routers
from domain.aggregates.views import StudentSerializedView

# ---------------------------------------------------- #

router = routers.DefaultRouter()
router.register("students", StudentSerializedView, "api_view_list")

urlpatterns = [
    path("", homepage, name="home"),
    path("plustwo/", plustwo, name="plustwo"),
    path("contact/", contact, name="contact"),
    path("termwise/", termwise, name="termwise"),
    path("result/", get_result, name="get_term"),
    path("api/termwise/", json_termwise, name="api_termwise"),
    path("annual/", annual_result, name="annual_result"),
    path("annual-result/", get_annual, name="get_annual"),
    path("get-classes/", get_classes, name="get-classes"),
    path("api/", include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
