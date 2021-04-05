from django import forms
from .Module import Module
from .File import File

class ModulesForm(forms.ModelForm):

    class Meta:
        model = Module
        fields = ['modulename']

    def getModuleName(self):
        return self.cleaned_data['modulename']
    
    def getModuleID(self):
        return self.data['module_id']


class FilesForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ['files']
    
    def getFiles(self):
        return self.cleaned_data["files"]

    def getFileID(self):
        return self.data["fileID"]

