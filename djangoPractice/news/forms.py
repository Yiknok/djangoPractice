from django import forms
from .models import News
from django.core.exceptions import ValidationError

import re


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5,}),
            'category': forms.Select( attrs={'class': 'form-control',}),
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title ):
            raise ValidationError('title haven`t to start from number')
        return title
    def clean_is_published(self):
        is_published=self.cleaned_data['is_published']
        if not is_published :
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
