from django import forms
from .Activity import *

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['act_name','act_description','act_photo','act_venue','act_date', 'interests']
    
    def getName(self):
        return self.data['act_name']
    def getDescription(self):
        return self.data['act_description']
    def getPhoto(self):
        return self.cleaned_data['act_photo']
    def getVenue(self):
        return self.data['act_venue']
    def getDate(self):
        return self.cleaned_data['act_date']
    def getInterests(self):
        return self.data.getlist('interests')
    def getId(self):
        return self.data['id']