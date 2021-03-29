from django import forms
from .models import Module, File

class ModulesForm(forms.ModelForm):

    class Meta:
        model = Module
        fields = ['modulename']

class FilesForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ['files']



