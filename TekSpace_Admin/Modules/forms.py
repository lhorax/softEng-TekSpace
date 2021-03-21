from django import forms
from .models import Modules, Files

class ModulesForm(forms.ModelForm):

    class Meta:
        model = Modules
        fields = ['modulename']

class FilesForm(forms.ModelForm):

    class Meta:
        model = Files
        fields = ['files']



