from django import forms
from .models import Document, Post, Images, Category
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text', 
            'image',
            'tags',
        ]

# class PictureWidget(forms.widgets.Widget):
#     def render(self, name, value, attrs=None):
#         if str(value) == '':
#             html1 = "<img id='id_image' style='display:block' class='rounded float-left d-block'/>"
#         else:
#             html1 = "<img id='id_image' style='display:block' class='rounded float-left d-block' src='" + settings.MEDIA_URL + str(value) + "'/>"
#         return mark_safe(html1)

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'image',
            'tags',
        ]

class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = [ 'image' ]
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Upload Pic(s)', css_class='btn-primary'))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'multiple':True})
        