from django import forms
from .models import *

class TaskForm(forms.ModelForm):

    class Meta:
        model = Tasks
        fields = ['task_title', 'task_description', 'task_totalScore', 'task_dateDue', 'task_dueTime', 'task_file']

class UpdateForm(forms.ModelForm):

	class Meta:
		model = Student_Session_Task
		fields = ['feedback', 'actualScore']

#class FilesForm(forms.ModelForm):
#
 #   class Meta:
  #      model = TaskFile
   #     fields = ['file']
