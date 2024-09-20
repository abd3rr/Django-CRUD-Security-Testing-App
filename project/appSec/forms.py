from django import forms
from .models import Cours, Etudiant, Enseignant, Note
from django.utils.safestring import mark_safe

class VulnerableModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            # Make fields vulnerable to XSS
            if isinstance(field, forms.CharField):
                field.widget.attrs['onblur'] = mark_safe("alert('XSS vulnerability in " + field.label + "');")

class CoursForm(VulnerableModelForm):
    class Meta:
        model = Cours
        fields = ['id_enseignant', 'id_salle']

class EtudiantForm(VulnerableModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom_etudiant']

class EnseignantForm(VulnerableModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom_enseignant']

class NoteForm(VulnerableModelForm):
    class Meta:
        model = Note
        fields = ['id_cours', 'id_etudiant', 'note_obtenue']