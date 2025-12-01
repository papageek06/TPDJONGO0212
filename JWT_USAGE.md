# Guide d'utilisation de JWT

## Configuration JWT

L'authentification JWT est configurée dans le projet. Toutes les API nécessitent une authentification.

## Endpoints JWT

### 1. Obtenir un token d'accès (Login)
**POST** `/api/token/`

Body (JSON):
```json
{
    "username": "votre_username",
    "password": "votre_password"
}
```

Réponse:
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### 2. Rafraîchir le token
**POST** `/api/token/refresh/`

Body (JSON):
```json
{
    "refresh": "votre_refresh_token"
}
```

Réponse:
```json
{
    "access": "nouveau_access_token"
}
```

### 3. Vérifier un token
**POST** `/api/token/verify/`

Body (JSON):
```json
{
    "token": "votre_token"
}
```

## Utilisation des tokens

Pour accéder aux endpoints protégés, incluez le token dans l'en-tête Authorization :

```
Authorization: Bearer votre_access_token
```

## Endpoints API disponibles

Tous ces endpoints nécessitent une authentification JWT :

- `GET/POST /api/voitures/` - Liste et création de voitures
- `GET/PUT/DELETE /api/voitures/<id>/` - Détails d'une voiture
- `GET/POST /api/clients/` - Liste et création de clients
- `GET/PUT/DELETE /api/clients/<id>/` - Détails d'un client
- `GET/POST /api/locations/` - Liste et création de locations
- `GET/PUT/DELETE /api/locations/<id>/` - Détails d'une location
- `GET /api/me/` - Informations de l'utilisateur connecté

## Exemple avec cURL

### 1. Obtenir un token
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "votre_password"}'
```

### 2. Utiliser le token pour accéder à l'API
```bash
curl -X GET http://127.0.0.1:8000/api/voitures/ \
  -H "Authorization: Bearer votre_access_token"
```

## Durée de vie des tokens

- **Access Token** : 1 heure
- **Refresh Token** : 1 jour

## Créer un utilisateur de test

Pour tester l'API, créez un superutilisateur :

```bash
python manage.py createsuperuser
```

Ou créez un utilisateur normal via l'interface d'administration Django.

