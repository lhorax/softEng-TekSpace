from django.db import models
from Students.Student import Student
from Accounts .models import CustomUser
from Sessions.Session import Session
from django.core.validators import FileExtensionValidator
import datetime
from .Tasks import Tasks

class Student_Session_Task(models.Model):
	id = models.AutoField(primary_key=True)
	student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
	feedback = models.CharField(max_length=300, default="No Feedback")
	file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True, blank=True)
	actualScore = models.IntegerField(default=0, null=True)
	isSubmitted = models.BooleanField(default = False)
	isGraded = models.BooleanField(default = False)
	dateSubmitted = models.DateField(default=datetime.date.today)
	task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
	session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)

	def getExamine(sid):
		return Student_Session_Task.objects.filter(sessions_id=sid)

	# def addExamine(feedback, file, filename, actualScore, isSubmitted):
	# 	new_exam = Student_Session_Task()
	# 	new_exam.feedback = feedback
	# 	new_exam.file = file
	# 	new_exam.filename = filename
	# 	new_exam.actualScore = actualScore
	# 	new_exam.isSubmitted = isSubmitted
	# 	new_task.save()

	def addStudentExam(student, task, session):
		#print("hello")
		new_exam = Student_Session_Task()
		new_exam.student = student
		new_exam.task = task
		new_exam.session = session
		new_exam.save()

	def getExam(student_id, task_id):
		return Student_Session_Task.objects.get(student_id = student_id, task_id=task_id)

	def updateExam(student_id, feedback, actualScore):
		examine = Student_Session_Task.objects.filter(student_id = student_id).update(feedback = feedback, actualScore = actualScore, isGraded = True)

	class Meta:
		db_table = "Student_Session_Task"