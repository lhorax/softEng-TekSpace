from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Interest'
urlpatterns = [ 
    path('', views.index, name="index_view"),
    path('create/',views.interest_create, name="interest_create"),
    path('view/<str:name>', views.interest_view, name="interest_view"),
    path('update/', views.interest_update, name="interest_update"),
    path('delete/', views.interest_delete, name="interest_delete"),
]