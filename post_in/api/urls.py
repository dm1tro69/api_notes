from .views import *
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('notes/', NotesListView.as_view()),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='notes-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
