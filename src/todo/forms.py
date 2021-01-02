from django import forms
from django.forms import fields
from .models import Todo

class TodoAddForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title',)
        