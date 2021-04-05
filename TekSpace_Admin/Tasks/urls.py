from django.urls import path
from .TaskView import TaskView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Tasks'
urlpatterns = [ 
    path('', TaskView.viewTasks, name="index"),
    path('create/', TaskView.createTask, name="create_task"),
    path('delete/', TaskView.deleteTask, name="delete_task"),
    path('view/<str:id>', TaskView.viewSpecificTask, name="view_task"),
    path('details/<str:id>', TaskView.viewDetails, name="view_details"),
    path('examine/<str:student_id>', TaskView.examDetails, name="exam_details"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)