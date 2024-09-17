from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Cours)
admin.site.register(models.Etudiant)
admin.site.register(models.Note)
admin.site.register(models.Enseignant)
admin.site.register(models.Salle)

