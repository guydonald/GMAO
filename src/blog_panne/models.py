from django.db import models
from authentication.models import User

# Create your models here.

class OrderWork(models.Model):
    executant = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=150, unique=True)
    heure_debut = models.DateTimeField(null=True, blank=True)
    heure_fin = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.code

    def heure_debut_exists(self): 
        return self.heure_debut is not None 
    
    def heure_fin_exists(self): 
        return self.heure_fin is not None
    
class PieceUtilisee(models.Model):
    ETAT_PIECE_CHOICES = [ 
        ('NEUF', 'Neuf'), 
        ('RECYCLER', 'Recycler'),
    ]
    nom = models.CharField(max_length=150)
    nombre_utilisee = models.PositiveIntegerField()
    etat = models.CharField(max_length=50, choices=ETAT_PIECE_CHOICES, null=False)
    ordre_travail = models.ForeignKey(OrderWork, on_delete=models.CASCADE)

   
class Intervention(models.Model):
    ordre_travail = models.ForeignKey(OrderWork, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    actions = models.TextField()
    observation = models.TextField()
    classe_action = models.CharField(max_length=50, choices=[ ('AUTOMATISME', 'Automatisme'), ('PLOMBERIE', 'Plomberie'), ('ELECTRIQUE', 'Électrique'), ('MECANIQUE', 'Mécanique'), ('UTILITAIRE', 'Utilitaire'), ])
    pieces_utilisees = models.ManyToManyField(PieceUtilisee)

