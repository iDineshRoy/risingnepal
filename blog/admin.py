from django.contrib import admin
from .models import Post, Document, FeaturedPost, Images, Category

admin.site.register(Post)
admin.site.register(Document)
admin.site.register(FeaturedPost)
admin.site.register(Images)
admin.site.register(Category)
