from django import forms

from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='News title', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }))
    content = forms.CharField(label='News content', required=False, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': 5,
        }
    ))
    is_published = forms.BooleanField(label='News status', initial=True)
    category = forms.ModelChoiceField(empty_label='Choose news category', label='News category',
                                      queryset=Category.objects.all(), widget=forms.Select(
            attrs={
                'class': 'form-control',

            }
        ))
