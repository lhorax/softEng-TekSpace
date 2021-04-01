from django.db import models
from Students.Student import Student
from Accounts .models import CustomUser
from Sessions.Session import Session
from django.core.validators import FileExtensionValidator
import datetime

# Create your models here.
class Tasks(models.Model):
	task_id = models.AutoField(primary_key=True)
	task_title = models.CharField(max_length=20, blank=True)
	task_description = models.CharField(max_length=100, blank=True, null=True)
	task_dateDue = models.DateField(default=datetime.date.today, blank=True, null=True)
	task_dueTime = models.TimeField( blank=True, null=True)
	task_dateCreated = models.DateField(default=datetime.date.today)
	task_totalScore = models.IntegerField(default=0, blank=True, null=True)
	task_file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True, blank=True)
	sessions = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)

	def getLatestTask():
		return Tasks.objects.latest('task_id')

	def getTasks(sid):
		return Tasks.objects.filter(sessions_id=sid)

	def getSpecificTask(tid):
		return Tasks.objects.get(task_id=tid)
    
	def addTask(task_title, task_description, task_totalScore, task_dateDue, task_dueTime, task_file, session):
		try:
			new_task = Tasks()
			new_task.task_title = task_title
			new_task.task_description = task_description
			new_task.task_totalScore = task_totalScore
			new_task.task_dateDue = task_dateDue
			new_task.task_dueTime = task_dueTime
			if task_file != '':
				new_task.task_file = task_file
			new_task.sessions = session
			new_task.save()
		except Exception as e:
			print(e)

	def removeTask(id):
		query = Tasks.objects.get(pk=id)
		query.delete()

	class Meta:
		db_table = "Tasks"

#class Student_Session_Task(models.Model):
#	id = models.AutoField(primary_key=True)
#	student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
#	feedback = models.CharField(max_length=300, default="No Feedback")
#	file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True, blank=True)
#	actualScore = models.IntegerField(default=0, null=True)
#	isSubmitted = models.BooleanField(default = False)
#	isGraded = models.BooleanField(default = False)
#	dateSubmitted = models.DateField(default=datetime.date.today)
#	task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
#	session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)

#	def getExamine(sid):
#		return Student_Session_Task.objects.filter(sessions_id=sid)

	# def addExamine(feedback, file, filename, actualScore, isSubmitted):
	# 	new_exam = Student_Session_Task()
	# 	new_exam.feedback = feedback
	# 	new_exam.file = file
	# 	new_exam.filename = filename
	# 	new_exam.actualScore = actualScore
	# 	new_exam.isSubmitted = isSubmitted
	# 	new_task.save()

#	def addStudentExam(student, task, session):
		#print("hello")
#		new_exam = Student_Session_Task()
#		new_exam.student = student
#		new_exam.task = task
#		new_exam.session = session
#		new_exam.save()

#	def getExam(student_id, task_id):
#		return Student_Session_Task.objects.get(student_id = student_id, task_id=task_id)

#	def updateExam(student_id, feedback, actualScore):
#		examine = Student_Session_Task.objects.filter(student_id = student_id).update(feedback = feedback, actualScore = actualScore, isGraded = True)

#	class Meta:
#		db_table = "Student_Session_Task"

#class TaskFile(models.Model):
#	file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True)
#	filename = models.CharField(max_length=50, null=True)
#	task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
#
#	def getFiles(task_id):
#		return File.objects.filter(task_id=task_id)
#
#	def createTaskFile(id, file, filename):
#		new_file = Task_File()
#		new_file.task = Tasks.getTaskFile(id)
#		new_file.file = file
#		new_task.filename = filename
#		new_file.save()
#
#	class Meta:
#		db_table = "Task_File"

