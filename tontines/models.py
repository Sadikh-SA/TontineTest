from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from datetime import date    


# Create your models here.

cotisations = (
    (10, '10 jours'),
    (20, '20 jours'),
    (30, '30 jours'),
    (40, '40 jours'),
)

# Class pour le nom du tontine 
class nomTontine(models.Model):
    nom = models.CharField("Nom de la Tontine: ", max_length=120)
    dateDébut = models.DateField(("Date"), default=date.today, blank=True) 
    dateFin = models.DateField(("Date"), default=date.today, blank=True)
    cotisations = models.CharField("Cotisation par ", max_length= 15 ,choices=cotisations, blank=True, null=True)
    creerPar = models.ForeignKey(User, related_name='Ajoutar', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

#Class pour les adhérents
class adherents(models.Model):
    nom = models.CharField("Nom Complet de l'adhérent: ", max_length=120)
    adresse = models.CharField("Adresse Complet de l'adhérent: ", max_length=100)
    email = models.CharField("email de l'adhérent: ", max_length=100, blank = True, null = True)
    telephone = models.CharField("téléphone de l'adhérent: ", max_length=13)
    creerPar = models.ForeignKey(User, on_delete=models.CASCADE)
    dateCreation = models.DateField("Date de Création ", auto_now_add=True)
    statut = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

#Class pour la cotisation
class cotisation(models.Model):
    montant = models.DecimalField(decimal_places=2, max_digits=15)
    nomAderent = models.ForeignKey(adherents, related_name='nom_adherant', on_delete=models.CASCADE)
    dateAjoute = models.DateField("Date de Début ", auto_now_add=True) 

    def __str__(self):
        return self.montant