from django.core.management.base import BaseCommand
from concessionnaire.models import Concessionnaire, Vehicule


class Command(BaseCommand):
    help = 'Crée des données de test pour le concessionnaire'

    def handle(self, *args, **options):
        self.stdout.write('Creation des donnees de test...')
        
        # Nettoyer les données existantes (optionnel)
        Vehicule.objects.all().delete()
        Concessionnaire.objects.all().delete()
        
        # Créer des concessionnaires
        concessionnaires_data = [
            {'nom': 'AutoMax Paris', 'siret': '12345678901234'},
            {'nom': 'MotoCenter Lyon', 'siret': '98765432109876'},
            {'nom': 'Garage Moderne', 'siret': '11223344556677'},
            {'nom': 'Concession Premium', 'siret': '55667788990011'},
        ]
        
        concessionnaires = []
        for c_data in concessionnaires_data:
            concessionnaire = Concessionnaire.objects.create(
                nom=c_data['nom'],
                siret=c_data['siret']
            )
            concessionnaires.append(concessionnaire)
            self.stdout.write(self.style.SUCCESS(f'[OK] Concessionnaire cree: {concessionnaire}'))
        
        # Créer des véhicules
        vehicules_data = [
            # Concessionnaire 0 - AutoMax Paris
            {'type': 'auto', 'marque': 'Peugeot', 'chevaux': 110, 'prix_ht': 25000.00, 'concessionnaire': 0},
            {'type': 'auto', 'marque': 'Renault', 'chevaux': 90, 'prix_ht': 22000.00, 'concessionnaire': 0},
            {'type': 'auto', 'marque': 'Citroën', 'chevaux': 100, 'prix_ht': 23000.00, 'concessionnaire': 0},
            {'type': 'auto', 'marque': 'Volkswagen', 'chevaux': 150, 'prix_ht': 35000.00, 'concessionnaire': 0},
            # Concessionnaire 1 - MotoCenter Lyon
            {'type': 'moto', 'marque': 'Yamaha', 'chevaux': 120, 'prix_ht': 12000.00, 'concessionnaire': 1},
            {'type': 'moto', 'marque': 'Honda', 'chevaux': 100, 'prix_ht': 10000.00, 'concessionnaire': 1},
            {'type': 'moto', 'marque': 'Kawasaki', 'chevaux': 140, 'prix_ht': 15000.00, 'concessionnaire': 1},
            {'type': 'moto', 'marque': 'Suzuki', 'chevaux': 110, 'prix_ht': 11000.00, 'concessionnaire': 1},
            # Concessionnaire 2 - Garage Moderne
            {'type': 'auto', 'marque': 'BMW', 'chevaux': 200, 'prix_ht': 55000.00, 'concessionnaire': 2},
            {'type': 'auto', 'marque': 'Mercedes', 'chevaux': 220, 'prix_ht': 60000.00, 'concessionnaire': 2},
            {'type': 'auto', 'marque': 'Audi', 'chevaux': 190, 'prix_ht': 50000.00, 'concessionnaire': 2},
            # Concessionnaire 3 - Concession Premium
            {'type': 'auto', 'marque': 'Tesla', 'chevaux': 300, 'prix_ht': 70000.00, 'concessionnaire': 3},
            {'type': 'auto', 'marque': 'Porsche', 'chevaux': 350, 'prix_ht': 95000.00, 'concessionnaire': 3},
            {'type': 'moto', 'marque': 'Ducati', 'chevaux': 160, 'prix_ht': 20000.00, 'concessionnaire': 3},
        ]
        
        for v_data in vehicules_data:
            vehicule = Vehicule.objects.create(
                type=v_data['type'],
                marque=v_data['marque'],
                chevaux=v_data['chevaux'],
                prix_ht=v_data['prix_ht'],
                concessionnaire=concessionnaires[v_data['concessionnaire']]
            )
            self.stdout.write(self.style.SUCCESS(f'[OK] Vehicule cree: {vehicule}'))
        
        self.stdout.write(self.style.SUCCESS('\n[OK] Toutes les donnees de test ont ete creees avec succes!'))
        self.stdout.write(f'\nResume:')
        self.stdout.write(f'  - {Concessionnaire.objects.count()} concessionnaires')
        self.stdout.write(f'  - {Vehicule.objects.count()} vehicules')
