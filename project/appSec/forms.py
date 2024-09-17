from django import forms
from .models import Cours, Etudiant, Enseignant, Note

class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = ['id_enseignant', 'id_salle']

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom_etudiant']

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom_enseignant']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['id_cours', 'id_etudiant', 'note_obtenue']