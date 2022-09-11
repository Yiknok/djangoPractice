from django import forms
from .models import News
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

import re

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password',help_text='Password must contain letters and numbers',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, }),
            'category': forms.Select(attrs={'class': 'form-control', }),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('title haven`t to start from number')
        return title

    def clean_is_published(self):
        is_published = self.cleaned_data['is_published']
        if not is_published:
            raise ValidationError('you must accepted published param')
        return is_published

# from .models import Category
#
#
# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='News title', widget=forms.TextInput(
#         attrs={
#             'class': 'form-control',
#         }))
#     content = forms.CharField(label='News content', required=False, widget=forms.Textarea(
#         attrs={
#             'class': 'form-control',
#             'rows': 5,
#         }
#     ))
#     is_published = forms.BooleanField(label='News status', initial=True)
#     category = forms.ModelChoiceField(empty_label='Choose news category', label='News category',
#                                       queryset=Category.objects.all(), widget=forms.Select(
#             attrs={
#                 'class': 'form-control',
#
#             }
#         ))
