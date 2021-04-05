from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from Students.Student import Student
from Sessions.Session import Session
from Accounts .models import CustomUser
from Sessions.SessionForm import SessionForm
from django.db.models.query import QuerySet
from .TaskForm import TaskForm
from .UpdateForm import UpdateForm
from .Tasks import Tasks
from .Student_Session_Task import Student_Session_Task 
# Create your views here.

class TaskView(View):

	def viewTasks(request):
		#student = Student.objects.all()
		sid = request.session.get('sid')
		#session = Session.getSession(sid)
		context = {
			'Tasks' : Tasks.getTasks(sid),
			#'student':student,
			#'session' : session,
		}
		print(context)
		return render(request, 'Tasks/Session-Actions.html', context)

	def createTask(request):
		if request.method == 'POST':
			print(request.POST)
			if 'addTaskBtn' in request.POST:
				print("add")
				sid = request.session.get('sid')
				session = Session.getSession(sid)
				form = TaskForm(request.POST, request.FILES)
				if form.is_valid():
					task_title = form.getTaskTitle()
					task_description = form.getTaskDescription()
					task_totalScore = form.getTaskTotalScore()
					task_dateDue = form.getTaskDateDue()
					task_dueTime = form.getTaskDueTime()
					task_file = form.getTaskFile()
					Tasks.addTask(task_title, task_description, task_totalScore, task_dateDue, task_dueTime, task_file, session)

					task = Tasks.getLatestTask()
					students = session.students.all()
					for student in students:
						print(student)
						Student_Session_Task.addStudentExam(student, task, session)

					messages.success(request, ("Task Successfully Added"))
				else:
					print(form.errors)

			return redirect("Tasks:index")

	def deleteTask(request):
		if request.method == 'POST':
			print(request.POST)
			if 'deleteTaskBtn' in request.POST:
				form = TaskForm(request.POST or None)
				tid = form.getTaskId()
				Tasks.removeTask(tid)
				messages.success(request, ("Task Successfully Deleted"))

			return redirect("Tasks:index")

	def goToSessionsPageBtn(request):
		if request.method == 'POST':
			print(request.POST)
			return redirect("Sessions:index_view")

	# former class TaskView
	def viewSpecificTask(request, id):
		sid = request.session.get('sid')
		request.session['tid'] = id
		student = Student.objects.all()
		task = Tasks.getSpecificTask(id)
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
		return render(request, 'Tasks/TaskView.html',context)

	# former class TaskDetails
	def viewDetails(request, id):
		task = Tasks.getSpecificTask(id)
		context = {
			'task': task
		}
		print(context)
		return render(request, 'Tasks/TaskDetails.html', context)
	
	# former class TaskExamine
	def examDetails(request, student_id):
		tid = request.session.get('tid')
		if request.method == 'GET':
			task = Tasks.getSpecificTask(tid)
			stud_task = Student_Session_Task.getExam(student_id, tid)
			context = {
				'stud_task': stud_task,
				'task': task
			}
			return render(request, 'Tasks/TaskExamine.html', context)

		if request.method == 'POST':
			if 'updateBtn' in request.POST:
				stud_task = Student_Session_Task.getExam(student_id, tid)
				form = UpdateForm(request.POST, instance=stud_task)
				if form.is_valid():
					feedback = form.getStudentSessionTaskFeedback()
					score = form.getStudentSessionTaskActualScore()
					Student_Session_Task.updateExam(student_id, feedback, score)
					messages.success(request, ("Evaluated Successfully"))
					return redirect('Tasks:view_task', stud_task.task_id)
				else:
					print(form.errors)
					messages.success(request, ("Sorry, there was an error during evaluation"))
			return redirect('Tasks:exam_details', student_id)