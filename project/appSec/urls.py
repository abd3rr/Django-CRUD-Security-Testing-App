from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Cours URLs
    path('cours/', views.CoursListView.as_view(), name='cours_list'),
    path('cours/new/', views.CoursCreateView.as_view(), name='cours_create'),
    path('cours/<int:pk>/edit/', views.CoursUpdateView.as_view(), name='cours_update'),
    path('cours/<int:pk>/delete/', views.CoursDeleteView.as_view(), name='cours_delete'),
    
    # Etudiant URLs
    path('etudiants/', views.EtudiantListView.as_view(), name='etudiant_list'),
    path('etudiants/new/', views.EtudiantCreateView.as_view(), name='etudiant_create'),
    path('etudiants/<int:pk>/edit/', views.EtudiantUpdateView.as_view(), name='etudiant_update'),
    path('etudiants/<int:pk>/delete/', views.EtudiantDeleteView.as_view(), name='etudiant_delete'),
    
    # Enseignant URLs
    path('enseignants/', views.EnseignantListView.as_view(), name='enseignant_list'),
    path('enseignants/new/', views.EnseignantCreateView.as_view(), name='enseignant_create'),
    path('enseignants/<int:pk>/edit/', views.EnseignantUpdateView.as_view(), name='enseignant_update'),
    path('enseignants/<int:pk>/delete/', views.EnseignantDeleteView.as_view(), name='enseignant_delete'),
    
    # Note URLs
    path('notes/', views.NoteListView.as_view(), name='note_list'),
    path('notes/new/', views.NoteCreateView.as_view(), name='note_create'),
    path('notes/<int:pk>/edit/', views.NoteUpdateView.as_view(), name='note_update'),
    path('notes/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note_delete'),
]