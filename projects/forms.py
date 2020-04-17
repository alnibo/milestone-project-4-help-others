from django import forms
from .models import Project


class AddProjectForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
                           {'placeholder': 'Sample Project'}),
                           required=True)
    category = forms.CharField(widget=forms.TextInput(
                               {'placeholder': 'Education'}),
                               required=True)
    description = forms.CharField(widget=forms.TextInput(
                                  {'placeholder': 'Education'}),
                                  required=True)

    class Meta:
        model = Project
        fields = ('name', 'category', 'description')
