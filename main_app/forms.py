from .models import Comment, Art
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', 'rating', 'date_created')
