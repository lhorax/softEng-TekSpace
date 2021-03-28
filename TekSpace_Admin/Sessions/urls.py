from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'Sessions'
urlpatterns = [ 
    path('', views.SessionsView.as_view(), name="index_view"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)