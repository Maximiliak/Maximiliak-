from django.urls import path
from . import views

urlpatterns = [
    path('notes/<int:notes_id>/', views.index, name = 'notes' ), #http://127.0.0.1:8000/notes/
    path('max/', views.index,name='max') #http://127.0.0.1:8000/max/
]
