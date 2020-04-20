from django import forms
from .models import Project


class AddProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        exclude = ['added_by']
