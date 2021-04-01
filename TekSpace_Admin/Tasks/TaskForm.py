from django import forms
from .Tasks import Tasks

class TaskForm(forms.ModelForm):

    class Meta:
        model = Tasks
        fields = ['task_title', 'task_description', 'task_totalScore', 'task_dateDue', 'task_dueTime', 'task_file']

    def getTaskId(self):
    	return self.data['task_id']

    def getTaskTitle(self):
    	return self.data['task_title']

    def getTaskDescription(self):
    	return self.cleaned_data['task_description']

    def getTaskTotalScore(self):
    	return self.cleaned_data['task_totalScore']

    def getTaskDateDue(self):
    	return self.cleaned_data['task_dateDue']

    def getTaskDueTime(self):
    	return self.cleaned_data['task_dueTime']

    def getTaskFile(self):
    	return self.cleaned_data['task_file']
