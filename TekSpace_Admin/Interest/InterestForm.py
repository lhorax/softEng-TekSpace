from django import forms
from .Interest import Interest


class InterestForm(forms.ModelForm):

    class Meta:
        model = Interest
        fields = ['int_name','int_description','int_photo']
    
    def getName(self):
        return self.data['int_name']
    
    def getDescription(self):
        return self.data['int_description']

    def getPhoto(self):
        return self.cleaned_data['int_photo']
    
    # def getName(self):
    #     return self.data['name']

    def getId(self):
        return self.data['id']