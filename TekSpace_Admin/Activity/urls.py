from django.urls import path
from .ActivityView import ActivityView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Activity'
urlpatterns = [ 
    path('', ActivityView.index, name="index_view"),
    path('create/',ActivityView.activity_create, name="activity_create"),
    path('view/<str:name>', ActivityView.activity_view, name="activity_view"),
    path('update/', ActivityView.activity_update, name="activity_update"),
    path('delete/', ActivityView.activity_delete, name="activity_delete"),
]