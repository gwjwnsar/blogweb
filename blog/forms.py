from django import forms
from django.utils import timezone
from datetime import datetime

class PostForm(forms.Form):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = forms.CharField(label='Title', max_length=250)
    slug = forms.SlugField(label='Slug', max_length=250)
    content = forms.CharField(label='Content',widget=forms.Textarea)
    publish = forms.DateTimeField(label='Published Date',initial=datetime.now())
    status = forms.ChoiceField(widget=forms.RadioSelect, choices=STATUS_CHOICES)
