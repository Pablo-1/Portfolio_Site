from django import forms
from .models import Feedback
from django.forms import TextInput, Textarea

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'alias',
            'feedback'
        ]
        widgets = {
            'alias': TextInput(attrs={
                'class':"form-control",
                'style':'max-width:300px;',
                'placeholder':'Alias'
            }),
            'feedback':Textarea(attrs={
                'class':"form-control",
                'style':'max-width:600px;',
                'style':'max-height:200px',
                'placeholder':'Your feedback goes here'
            })
        }
