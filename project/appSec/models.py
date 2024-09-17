from django.db import models

class Enseignant(models.Model):
    id_enseignant = models.AutoField(primary_key=True)
    nom_enseignant = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_enseignant

class Salle(models.Model):
    id_salle = models.AutoField(primary_key=True)
    nom_salle = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_salle

class Cours(models.Model):
    id_cours = models.AutoField(primary_key=True)
    id_enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    id_salle = models.ForeignKey(Salle, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cours {self.id_cours}"

class Etudiant(models.Model):
    id_etudiant = models.AutoField(primary_key=True)
    nom_etudiant = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_etudiant

class Note(models.Model):
    id_cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    id_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    note_obtenue = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"Note for {self.id_etudiant} in {self.id_cours}"