from django.db import models
from django.core.validators import MinValueValidator, RegexValidator


class Concessionnaire(models.Model):
    """Modèle représentant un concessionnaire"""
    nom = models.CharField(max_length=64)
    siret = models.CharField(
        max_length=14,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{14}$',
                message='Le SIRET doit contenir exactement 14 chiffres'
            )
        ]
    )
    
    class Meta:
        verbose_name = "Concessionnaire"
        verbose_name_plural = "Concessionnaires"
        ordering = ['nom']
    
    def __str__(self):
        return f"{self.nom} (SIRET: {self.siret})"


class Vehicule(models.Model):
    """Modèle représentant un véhicule"""
    TYPE_CHOICES = [
        ('moto', 'Moto'),
        ('auto', 'Auto'),
    ]
    
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    marque = models.CharField(max_length=64)
    chevaux = models.IntegerField(validators=[MinValueValidator(1)])
    prix_ht = models.FloatField(validators=[MinValueValidator(0)])
    concessionnaire = models.ForeignKey(
        Concessionnaire,
        on_delete=models.CASCADE,
        related_name='vehicules'
    )
    
    class Meta:
        verbose_name = "Véhicule"
        verbose_name_plural = "Véhicules"
        ordering = ['marque', 'type']
    
    def __str__(self):
        return f"{self.marque} ({self.get_type_display()}) - {self.chevaux}ch"
