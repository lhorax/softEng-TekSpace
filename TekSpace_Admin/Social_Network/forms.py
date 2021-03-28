from django import forms
from .models import *

class SNIntForm(forms.ModelForm):

    class Meta:
        model = Interest
        fields = ('int_name','int_description','int_photo')

class SNActForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('act_name','act_description','act_photo','act_venue','act_date')