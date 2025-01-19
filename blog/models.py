from django.conf import settings
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, max_length=250)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextField()
    slug = models.SlugField(unique=True, max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, null=True, blank=True)
    tags = TaggableManager()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    featured = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.title

class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    caption = models.CharField(blank=True, max_length=140)
    #file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class FeaturedPost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    startdate = models.DateField()
    enddate = models.DateField()