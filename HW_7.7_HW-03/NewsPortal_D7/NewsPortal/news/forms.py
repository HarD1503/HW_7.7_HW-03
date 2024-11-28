from django import forms
from django.core.exceptions import ValidationError
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'post_author',
            #'post_type',
            #'post_time',
            'post_category',
            'post_title',
            'post_text',
            #'post_rating',
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("post_text")
        title = cleaned_data.get("post_title")
        if title == text:
            raise ValidationError("Заголовок не должен быть идентичен тексту.")
        return cleaned_data