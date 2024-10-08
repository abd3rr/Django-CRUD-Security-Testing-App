from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cours, Etudiant, Enseignant, Note
from .forms import CoursForm, EtudiantForm, EnseignantForm, NoteForm
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.views import View

def index(request):
    cours = Cours.objects.all()
    etudiants = Etudiant.objects.all()
    enseignants = Enseignant.objects.all()
    notes = Note.objects.all()
    
    context = {
        'cours': cours,
        'etudiants': etudiants,
        'enseignants': enseignants,
        'notes': notes,
    }
    return render(request, 'index.html', context)

# Cours views
class CoursListView(ListView):
    model = Cours
    template_name = 'cours_list.html'
    context_object_name = 'cours'


class CoursCreateView(CreateView):
    model = Cours
    form_class = CoursForm
    template_name = 'cours_form.html'
    success_url = reverse_lazy('cours_list')

class CoursUpdateView(UpdateView):
    model = Cours
    form_class = CoursForm
    template_name = 'cours_form.html'
    success_url = reverse_lazy('cours_list')

class CoursDeleteView(DeleteView):
    model = Cours
    template_name = 'cours_confirm_delete.html'
    success_url = reverse_lazy('cours_list')

# Etudiant views
#class EtudiantListView(ListView):
#    model = Etudiant
#    print("im here")
#    template_name = 'etudiant_list.html'
#    context_object_name = 'etudiants'

class EtudiantCreateView(CreateView):
    model = Etudiant
    form_class = EtudiantForm
    template_name = 'etudiant_form.html'
    success_url = reverse_lazy('etudiant_list')

class EtudiantUpdateView(UpdateView):
    model = Etudiant
    form_class = EtudiantForm
    template_name = 'etudiant_form.html'
    success_url = reverse_lazy('etudiant_list')

class EtudiantDeleteView(DeleteView):
    model = Etudiant
    template_name = 'etudiant_confirm_delete.html'
    success_url = reverse_lazy('etudiant_list')
# vul ---
class VulnerableEtudiantListView(View):
    def get(self, request):
        search_term = request.GET.get('search', '').strip()  # Get the search term and strip any whitespace
       
        etudiants = []  # Initialize empty list
        
        print("var dump")
        print(vars(search_term))
        print(search_term)
        # Only execute the query if the search term is not empty
        if search_term:  # This will check if the search_term is not an empty string
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT id_etudiant, nom_etudiant FROM appSec_etudiant WHERE nom_etudiant LIKE '%{search_term}%'")
                columns = [col[0] for col in cursor.description]
                etudiants = [
                    dict(zip(columns, row))
                    for row in cursor.fetchall()
                ]
        
        context = {
            'etudiants': etudiants,
            'search_term': search_term  # Pass search term for display in HTML
        }
        return render(request, 'etudiant_list.html', context)



    def get(self, request):
        search_term = request.GET.get('search', '')
        
        # Vulnerable SQL query
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT id_etudiant, nom_etudiant FROM appSec_etudiant WHERE nom_etudiant LIKE '%{search_term}%'")
            columns = [col[0] for col in cursor.description]
            etudiants = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
        
        context = {
            'etudiants': etudiants,
        }
        return render(request, 'etudiant_list.html', context)    

# Enseignant views
class EnseignantListView(ListView):
    model = Enseignant
    template_name = 'enseignant_list.html'
    context_object_name = 'enseignants'

class EnseignantCreateView(CreateView):
    model = Enseignant
    form_class = EnseignantForm
    template_name = 'enseignant_form.html'
    success_url = reverse_lazy('enseignant_list')

class EnseignantUpdateView(UpdateView):
    model = Enseignant
    form_class = EnseignantForm
    template_name = 'enseignant_form.html'
    success_url = reverse_lazy('enseignant_list')

class EnseignantDeleteView(DeleteView):
    model = Enseignant
    template_name = 'enseignant_confirm_delete.html'
    success_url = reverse_lazy('enseignant_list')

# Note views
class NoteListView(ListView):
    model = Note
    template_name = 'note_list.html'
    context_object_name = 'notes'

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note_list')

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note_list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_confirm_delete.html'
    success_url = reverse_lazy('note_list')