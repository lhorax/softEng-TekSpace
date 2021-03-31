from django.urls import path
from .ModulesView import ModulesView
from django.conf.urls.static import static
from django.conf import settings


app_name = 'Modules'
urlpatterns = [ 
    path('', ModulesView.as_view(), name="index_view"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)