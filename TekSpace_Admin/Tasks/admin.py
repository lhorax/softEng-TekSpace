from django.contrib import admin
from .Tasks import Tasks
from. Student_Session_Task import Student_Session_Task

# Register your models here.
admin.site.register(Tasks)
admin.site.register(Student_Session_Task)
#admin.site.register(TaskFile)
