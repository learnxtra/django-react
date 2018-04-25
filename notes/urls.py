from django.urls import path

from . import views 

urlpatterns = [
  path('', views.NoteList.as_view()),
  path('<int:pk>/', views.NoteDetail.as_view()) #api/v1/notes/1
]