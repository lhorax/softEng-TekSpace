from django.urls import path
from .views import TaskView
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'Tasks'
urlpatterns = [ 
    path('', views.TaskView.as_view(), name="index"),
    path('view/<str:id>', views.TaskView.viewSpecificTask, name="view_task"),
    path('details/<str:id>', views.TaskView.viewDetails, name="view_details"),
    path('examine/<str:student_id>', views.TaskView.examDetails, name="exam_details"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)