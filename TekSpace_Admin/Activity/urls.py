from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Activity'
urlpatterns = [ 
    path('', views.index, name="index_view"),
    path('create/',views.activity_create, name="activity_create"),
    path('view/<str:name>', views.activity_view, name="activity_view"),
    path('update/', views.activity_update, name="activity_update"),
    path('delete/', views.activity_delete, name="activity_delete"),
]