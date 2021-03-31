from django import forms
from .Module import Module
from .File import File

class ModulesForm(forms.ModelForm):

    class Meta:
        model = Module
        fields = ['modulename']

class FilesForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ['files']



