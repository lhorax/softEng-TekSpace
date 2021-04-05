from django.urls import path
from .SessionsView import SessionsView
from django.conf.urls.static import static
from django.conf import settings


app_name = 'Sessions'
urlpatterns = [ 
    path('', SessionsView.viewSessions, name="index_view"),
    path('create/', SessionsView.createSession, name="create_session"),
    path('delete/', SessionsView.deleteSession, name="delete_session"),
    path('scan/', SessionsView.goToSessionPage, name="scan_session"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)