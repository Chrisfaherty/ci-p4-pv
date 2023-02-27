from .models import Comment
from django import forms

# This is the form that is on the blogpage where the user submits their comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)