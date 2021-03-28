from django import forms
from .models import *


class InterestForm(forms.ModelForm):

    class Meta:
        model = Interest
        fields = ['int_name','int_description','int_photo']