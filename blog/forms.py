from pyexpat import model
import django


from django import forms

from . models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'body')