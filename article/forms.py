
from django import forms

from article.models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['todo']

        labels = {
            'todo' : '',
        }

        Widgets = {
            'todo' : forms.TextInput(attrs={'placeholder' : '할일을 입력해 주세요.'})


        }