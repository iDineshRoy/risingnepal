from django import forms
from .models import Document, Post, Images, Category
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

class PostForm(forms.ModelForm):
    choice = [('Draft', 'Draft'),('Published', 'Published')]
    feature = [('Not Featured', 'Not Featured'),('Featured', 'Featured')]
    status= forms.ChoiceField(choices=choice, widget=forms.Select(attrs={'id': 'status', 'name':'status', 'class':"btn btn-secondary dropdown-toggle"}))
    featured = forms.ChoiceField(choices=feature, widget=forms.Select(attrs={'id': 'featured', 'name':'featured', 'class':"btn btn-secondary dropdown-toggle"}))
    class Meta:
        model = Post
        fields = [
            'title',
            'text', 
            'image',
            'category',
            'tags',
            'status',
            'featured'
        ]
    # helper = FormHelper()
    # helper.form_method = 'POST'
    # helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['tags'].widget.attrs.update({'data-role':"tagsinput", 'type':'text', 'class':'form-control', 'id':'tagtest'})

class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None):
        if str(value) == '':
            html1 = "<img id='id_image' style='display:block' class='rounded float-left d-block'/>"
        else:
            html1 = "<img id='id_image' style='display:block' class='rounded float-left d-block' src='" + settings.MEDIA_URL + str(value) + "'/>"
        return mark_safe(html1)

class UpdatePostForm(forms.ModelForm):
    choice = [('Draft', 'Draft'),('Published', 'Published')]
    feature = [('Not Featured', 'Not Featured'),('Featured', 'Featured')]
    status= forms.ChoiceField(choices=choice, widget=forms.Select(attrs={'id': 'status', 'name':'status', 'class':"btn btn-secondary dropdown-toggle"}))
    featured = forms.ChoiceField(choices=feature, widget=forms.Select(attrs={'id': 'featured', 'name':'featured', 'class':"btn btn-secondary dropdown-toggle"}))
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'image',
            'category', 
            'tags',
            'status',
            'featured'
        ]
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Update Post', css_class='btn-primary'))

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
        