from django import forms
from .models import Idea

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'photo', 'content', 'devtool', 'interest']
        labels = {
            'title': '아이디어명',
            'photo': 'image',
            'content': '아이디어 설명',
            'devtool': '예상 개발툴',
            'interest': '아이디어 관심도',
        }