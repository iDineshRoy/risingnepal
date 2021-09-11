from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.posts, name='posts'),
    path('upload/', views.model_form_upload, name='upload'),
    path('new_post/', views.create_post, name='newpost'),
    path('update_post/<slug:slug>', views.update_post, name='update_post'),
    path('categories/', views.all_categories, name='allcategories'),
    path('new_category/', views.create_category, name='newcategory'),
    path('update_category/<slug:slug>', views.update_category, name='update_category'),
    path('tag/<slug:slug>', views.tagged, name='tagged'),
    path('category/<slug:slug>', views.show_post_category, name='catpost'),
    path('post/<slug:slug>', views.showpost, name='post'),
    path('edit-about/', views.edit_about, name='edit-about'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)