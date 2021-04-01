from django import forms
from .models import *

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['act_name','act_description','act_photo','act_venue','act_date', 'interests']