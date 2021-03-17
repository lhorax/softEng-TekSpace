from django import forms
from .models import Session

class SessionForm(forms.ModelForm):

    class Meta:
        model = Session
        fields = ['session_code', 'session_name']