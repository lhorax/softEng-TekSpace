from django import forms
from .Student_Session_Task import Student_Session_Task

class UpdateForm(forms.ModelForm):

	class Meta:
		model = Student_Session_Task
		fields = ['feedback', 'actualScore']

	def getStudentSessionTaskId(self):
		return self.data['id']

	def getStudentSessionTaskFeedback(self):
		return self.cleaned_data['feedback']

	def getStudentSessionTaskActualScore(self):
		return self.cleaned_data['actualScore']