# Documentation automatique de l'API

L'API REST est maintenant auto-découvrable grâce à **drf-spectacular** qui génère automatiquement une documentation OpenAPI/Swagger.

## Accès à la documentation

Une fois le serveur Django démarré, vous pouvez accéder à la documentation à plusieurs endroits :

### 1. Interface Swagger UI (Recommandé)
**URL** : http://127.0.0.1:8000/api/docs/

Interface interactive où vous pouvez :
- ✅ Voir tous les endpoints disponibles
- ✅ Tester les endpoints directement depuis le navigateur
- ✅ Voir les schémas de requête/réponse
- ✅ Authentifier avec JWT directement dans l'interface

### 2. Interface ReDoc
**URL** : http://127.0.0.1:8000/api/redoc/

Interface de documentation alternative avec une présentation différente.

### 3. Schéma OpenAPI (JSON/YAML)
**URL** : http://127.0.0.1:8000/api/schema/

Retourne le schéma OpenAPI au format JSON. Peut être utilisé avec d'autres outils comme Postman, Insomnia, etc.

## Utilisation de Swagger UI

### Étape 1 : Accéder à la documentation
1. Démarrez le serveur : `python manage.py runserver`
2. Ouvrez votre navigateur : http://127.0.0.1:8000/api/docs/

### Étape 2 : S'authentifier avec JWT
1. Cliquez sur le bouton **"Authorize"** en haut à droite
2. Dans le champ, entrez : `Bearer votre_access_token`
   - Pour obtenir un token, utilisez d'abord `/api/token/` avec vos identifiants
3. Cliquez sur **"Authorize"** puis **"Close"**

### Étape 3 : Tester les endpoints
1. Cliquez sur un endpoint pour l'étendre
2. Cliquez sur **"Try it out"**
3. Remplissez les paramètres si nécessaire
4. Cliquez sur **"Execute"**
5. Voyez la réponse en bas de la page

## Endpoints documentés

La documentation inclut automatiquement :

### Authentification
- `POST /api/token/` - Obtenir un token JWT
- `POST /api/token/refresh/` - Rafraîchir un token
- `POST /api/token/verify/` - Vérifier un token

### Voitures
- `GET /api/voitures/` - Liste toutes les voitures
- `POST /api/voitures/` - Créer une voiture
- `GET /api/voitures/{id}/` - Détails d'une voiture
- `PUT /api/voitures/{id}/` - Mettre à jour une voiture
- `DELETE /api/voitures/{id}/` - Supprimer une voiture

### Clients
- `GET /api/clients/` - Liste tous les clients
- `POST /api/clients/` - Créer un client
- `GET /api/clients/{id}/` - Détails d'un client
- `PUT /api/clients/{id}/` - Mettre à jour un client
- `DELETE /api/clients/{id}/` - Supprimer un client

### Locations
- `GET /api/locations/` - Liste toutes les locations
- `POST /api/locations/` - Créer une location
- `GET /api/locations/{id}/` - Détails d'une location
- `PUT /api/locations/{id}/` - Mettre à jour une location
- `DELETE /api/locations/{id}/` - Supprimer une location

### Utilisateur
- `GET /api/me/` - Informations de l'utilisateur connecté

## Avantages de la documentation automatique

✅ **Toujours à jour** : La documentation est générée automatiquement depuis votre code
✅ **Interactive** : Testez les endpoints directement depuis le navigateur
✅ **Complète** : Tous les schémas de données sont documentés
✅ **Standard** : Utilise OpenAPI 3.0, compatible avec de nombreux outils
✅ **Authentification intégrée** : Support JWT directement dans l'interface

## Import dans Postman

Vous pouvez importer le schéma OpenAPI dans Postman :

1. Récupérez le schéma : http://127.0.0.1:8000/api/schema/
2. Dans Postman : **Import** → **Link** → Collez l'URL
3. Toutes les routes seront importées automatiquement !

## Configuration

La configuration se trouve dans `config/settings.py` :

```python
SPECTACULAR_SETTINGS = {
    'TITLE': 'API Concessionnaire',
    'DESCRIPTION': 'API REST pour la gestion d\'un concessionnaire...',
    'VERSION': '1.0.0',
}
```

