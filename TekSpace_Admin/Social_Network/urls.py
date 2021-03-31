from django.urls import path
from .SocialNetworkView import SocialNetworkView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Social_Network'
urlpatterns = [ 
    path('', SocialNetworkView.index, name="index_view"),
]