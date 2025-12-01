from django.contrib import admin
from .models import Concessionnaire, Vehicule


@admin.register(Concessionnaire)
class ConcessionnaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'siret')
    search_fields = ('nom', 'siret')
    readonly_fields = ('siret',)  # SIRET visible dans l'admin mais non modifiable après création


@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('marque', 'type', 'chevaux', 'prix_ht', 'concessionnaire')
    list_filter = ('type', 'concessionnaire', 'marque')
    search_fields = ('marque', 'concessionnaire__nom')
    list_editable = ('prix_ht',)
