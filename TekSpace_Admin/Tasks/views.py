from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from .models import Tasks
from Students .models import Student
from Accounts .models import CustomUser
from django.db.models.query import QuerySet
from .forms import *
from .models import *
# Create your views here.

class TaskListView(View):
	def get(self, request):
		context = self.updateTemplate(request)
		return render(request, 'Tasks/Session-Actions.html', context)

	def post(self, request):
		if request.method == 'POST':
			print(request.POST)
			if 'addTaskBtn' in request.POST:
				form = TaskForm(request.POST, request.FILES)
				#form2 = FilesForm(request.POST, request.FILES, prefix="form2")
				if form.is_valid():
					self.createTask(request)
					print("valid1")
					messages.success(request, ("Task Successfully Added"))
				else:
					print(form.errors)

			if 'deleteTaskBtn' in request.POST:
				self.deleteTask(request)
				messages.success(request, ("Task Successfully Deleted"))
			
			if 'goToSessionsPageBtn' in request.POST:
				return redirect("Sessions:index_view")

			context = self.updateTemplate(request)
			return render(request, 'Tasks/Session-Actions.html', context)

	def viewTask(self, request):
		sid = request.session.get('sid')
		return Tasks.getTasks(sid)

	def createTask(self, request):
		task_title = request.POST.get('task_title')
		task_description = request.POST.get('task_description')
		task_totalScore = request.POST.get('task_totalScore')
		task_dateDue = request.POST.get('task_dateDue')
		task_dueTime = request.POST.get('task_dueTime')
		task_file = request.FILES['task_file']
		task_filename = request.FILES['task_file'].name
		sid = request.session.get('sid')
		session = Session.getSession(sid)
		Tasks.addTask(task_title, task_description, task_totalScore, task_dateDue, task_dueTime, task_file, task_filename, session)

	#def addTaskFile(self, request):
	#	task_id = request.POST.get('task_id')
		#file = request.FILES['file']
	#	filename = request.FILES['file'].name
	#	file = form.cleaned_data["file"]
	#	File.createTaskFile(task_id, file, filename)


	def deleteTask(self, request):
		sid = request.POST.get("task_id")
		print(sid)
		Tasks.removeTask(sid)

	def updateTemplate(self, request):
		student = Student.objects.all()
		return {'Tasks' : self.viewTask(request),
			'student':student,
		}


	def goToSessionActionsPage(self):
		pass

class TaskView(View):
	def get(self, request, id):
		sid = request.session.get('sid')
		print(sid)
		student = Student.objects.all()
		task = Tasks.objects.get(task_id = id)
		student_count = Student.objects.filter().count()
		stud_task = Student_Session_Task.objects.filter(task_id = id)

		context = {
			'task': task,
			'student': student,
			'student_count': student_count,
			'stud_task': stud_task,
		}
		context['to_grade'] = Student_Session_Task.objects.filter(isGraded=0, task_id = id).count()
		context['graded'] = Student_Session_Task.objects.filter(isGraded=1, task_id = id).count()
		print("50")
		print(context)
		return render(request, 'Tasks/TaskView.html',context)

	def post(self, request, id):
		if request.method == 'POST':
			if 'view_detailsBtn' in request.POST:
				context = self.view_details(request, id)
				print(context)
				# request.session['context']=context
				# print (context)
				return redirect('Tasks:view_details', id)

			if 'backBtn' in request.POST:
				return redirect("Tasks:view_task", id)

			# update template here
			task = Tasks.objects.get(task_id = id)
			context = {
				'task': task,
			}
			return render(request, 'Tasks/TaskView.html',context)
	
	def view_details(self, request, id):
		task = Tasks.objects.get(task_id = id)
		context = {
			'task': task
		}
		return context

	def exam_details(self, request, id):
		#eid = request.session.get('task_id')
		#print(eid)
		print("51")
		stud_task = Student_Session_Task.objects.filter(task_id = id)
		context = {
			'stud_task': stud_task,
		}
		return render(request, 'Tasks/TaskExamine.html',context)

class TaskDetails(View):
	def get(self, request, id):
		task = Tasks.objects.get(task_id = id)
		context = {
			'task': task
		}
		#context = request.session.get('context')
		print(context)
		return render(request, 'Tasks/TaskDetails.html', context)

	def task_details(self, request, id):
		task = Tasks.objects.get(task_id = id)
		context = {
			'task': task
		}
		return context

	def post(self, request, id):
		if 'closeBtn' in request.POST:
			return redirect("Tasks:view_task", id)

		if 'backBtn' in request.POST:
			return redirect("Tasks:view_task", id)


class TaskExamine(View):
	def get(self, request, student_id):
		#task = Tasks.objects.get(task_id = id1)
		stud_task = Student_Session_Task.objects.get(student_id = student_id)
		context = {
			#'task' : task,
			'stud_task': stud_task,
		}

		print("52")
		print(context)
		return render(request, 'Tasks/TaskExamine.html',context)

	def exam_details(self, request, student_id):
		stud_task = Student_Session_Task.objects.filter(student_id = student_id)
		context = {
			#'task' : task,
			'stud_task': stud_task,
		}
		print("53")
		print(context)
		return context

	def post(self, request, student_id):
		if request.method == 'POST':
			if 'updateBtn' in request.POST:
				stud_task = Student_Session_Task.objects.get(student_id = student_id)
				form = UpdateForm(request.POST, instance=stud_task)
				if form.is_valid():
					print("hello")
					feedback = request.POST.get('feedback')
					score = request.POST.get('actualScore')

					Student_Session_Task.updateExam(student_id, feedback, score)
					messages.success(request, ("Evaluated Successfully"))
					return redirect('Tasks:exam_details', student_id)
				else:
					print(form.errors)
					messages.success(request, ("Sorry, there was an error during evaluation"))
			return redirect('Tasks:exam_details', student_id)