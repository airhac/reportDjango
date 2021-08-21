from django.forms import ModelForm
from django import forms
from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height:auto;'}))
    #멀 mediumeditor로 만들고 싶은지에 대해 정보를 주기 위한 과정
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    #원래는 무조건 프로젝트를 고르게 되어있는데 프로젝트가 없어도 글을  쓸 수 있도록 하기 위해 사용

    class Meta:
        model = Article
        fields = ['title', 'image','project' ,'content']
