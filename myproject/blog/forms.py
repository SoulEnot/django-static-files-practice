from django import forms
from .models import Post
from django.utils import timezone


class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'created_at']
        # widgets = {
        #     'created_at': forms.DateInput(attrs={'type': 'date'})
        # }
        widgets = {
            'created_at': forms.DateInput({'type': 'date', 'value': timezone.now().strftime('%Y-%m-%d')})
        }

