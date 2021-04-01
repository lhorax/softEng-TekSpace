from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Social_Network'
urlpatterns = [ 
    path('', views.index, name="index_view"),
]