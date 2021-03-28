from django.urls import path
from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'Tasks'
urlpatterns = [ 
    path('', views.TaskListView.as_view(), name="index"),
    path('view/<str:id>', views.TaskView.as_view(), name="view_task"),
    path('details/<str:id>', views.TaskDetails.as_view(), name="view_details"),
    path('examine/<str:student_id>', views.TaskExamine.as_view(), name="exam_details"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)