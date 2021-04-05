from django import forms
from .Session import Session

class SessionForm(forms.ModelForm):
    
    class Meta:
        model = Session
        fields = ['session_code', 'session_name']

    def getSessionId(self):
        return self.data['session_id']

    def getSessionCode(self):
        return self.cleaned_data['session_code']

    def getSessionName(self):
        return self.cleaned_data['session_name']
