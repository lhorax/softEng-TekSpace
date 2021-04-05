from django.urls import path
from .InterestView import InterestView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Interest'
urlpatterns = [ 
    path('', InterestView.index, name="index_view"),
    path('create/',InterestView.interest_create, name="interest_create"),
    path('view/<str:name>', InterestView.interest_view, name="interest_view"),
    path('update/', InterestView.interest_update, name="interest_update"),
    path('delete/', InterestView.interest_delete, name="interest_delete"),
]

