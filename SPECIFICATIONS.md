# Spécifications du Projet - API Concessionnaire

## ✅ Modèles de données implémentés

### Concessionnaire
- ✅ `nom` : CharField(max_length=64)
- ✅ `siret` : CharField(max_length=14, unique=True, validation exacte de 14 chiffres)
- ✅ **SIRET non exposé dans l'API** (ni en lecture ni en écriture)

### Véhicule
- ✅ `type` : CharField avec choix entre "moto" et "auto"
- ✅ `marque` : CharField(max_length=64)
- ✅ `chevaux` : IntegerField (minimum 1)
- ✅ `prix_ht` : FloatField (minimum 0)
- ✅ `concessionnaire` : ForeignKey vers Concessionnaire

## ✅ Endpoints REST implémentés

### Endpoints obligatoires (GET uniquement)
- ✅ `GET /api/concessionnaires/` - Liste des concessionnaires
- ✅ `GET /api/concessionnaires/<id>/` - Détails d'un concessionnaire
- ✅ `GET /api/concessionnaires/<id>/vehicules/` - Liste des véhicules d'un concessionnaire
- ✅ `GET /api/concessionnaires/<id>/vehicules/<id>/` - Détails d'un véhicule

### Endpoints bonus
- ✅ `POST /api/users/` - Création d'un utilisateur
- ✅ `POST /api/token/` - Obtention d'un token JWT
- ✅ `POST /api/refresh_token/` - Rafraîchissement d'un token JWT (alias de /api/token/refresh/)

## ✅ Serializers

### ConcessionnaireSerializer
- ✅ Inclut : `id`, `nom`, `vehicules` (liste des véhicules)
- ✅ Exclut : `siret` (non exposé, ni en lecture ni en écriture)

### VehiculeSerializer
- ✅ Inclut : `id`, `type`, `marque`, `chevaux`, `prix_ht`, `concessionnaire`
- ✅ Tous les champs sont exposés

## ✅ Migrations

- ✅ Migrations générées et appliquées
- ✅ Base de données à jour

## ✅ Données de test

Commande pour créer des données de test :
```bash
python manage.py creer_donnees_test
```

Créé automatiquement :
- 4 concessionnaires
- 14 véhicules (motos et autos)

## ✅ Documentation automatique

- ✅ Swagger UI : http://127.0.0.1:8000/api/docs/
- ✅ ReDoc : http://127.0.0.1:8000/api/redoc/
- ✅ Schéma OpenAPI : http://127.0.0.1:8000/api/schema/

## ✅ Authentification JWT

- ✅ Configuration avec `djangorestframework-simplejwt`
- ✅ Access token : 1 heure
- ✅ Refresh token : 1 jour
- ✅ Endpoints d'authentification fonctionnels

## 📝 Structure du projet

Le projet est à la racine du dépôt avec :
- ✅ `.gitignore` configuré (exclut `__pycache__`, `.pyc`, `venv/`, etc.)
- ✅ `requirements.txt` avec toutes les dépendances
- ✅ Migrations dans `concessionnaire/migrations/`

## 🔍 Validation

Pour vérifier que tout fonctionne :

1. **Démarrer le serveur** :
```bash
python manage.py runserver
```

2. **Tester les endpoints** :
- http://127.0.0.1:8000/api/concessionnaires/
- http://127.0.0.1:8000/api/concessionnaires/1/
- http://127.0.0.1:8000/api/concessionnaires/1/vehicules/
- http://127.0.0.1:8000/api/concessionnaires/1/vehicules/1/

3. **Vérifier que le SIRET n'est pas exposé** :
- Le champ `siret` ne doit **jamais** apparaître dans les réponses JSON

4. **Tester l'authentification** :
```bash
POST /api/token/
{
    "username": "votre_username",
    "password": "votre_password"
}
```

## ✅ Conformité aux spécifications

- ✅ Structure du projet à la racine
- ✅ Modèles Concessionnaire et Véhicule conformes
- ✅ SIRET non exposé dans l'API
- ✅ Tous les endpoints obligatoires implémentés
- ✅ Endpoints bonus implémentés
- ✅ Serializers conformes
- ✅ Migrations générées et appliquées
- ✅ Documentation automatique (bonus)
- ✅ Authentification JWT (bonus)


