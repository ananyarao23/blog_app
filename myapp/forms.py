from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *

class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=FroalaEditor)
    class Meta:
        model = BlogModel
        fields = ['content']