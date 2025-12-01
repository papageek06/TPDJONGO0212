from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from .models import Concessionnaire, Vehicule
from .serializers import (
    ConcessionnaireSerializer,
    VehiculeSerializer,
    UserSerializer
)


@extend_schema(
    tags=['Concessionnaires'],
    summary='Liste des concessionnaires',
    description='Récupère la liste de tous les concessionnaires'
)
class ConcessionnaireListView(generics.ListAPIView):
    """
    Liste tous les concessionnaires.
    
    GET : Retourne la liste de tous les concessionnaires
    """
    queryset = Concessionnaire.objects.all()
    serializer_class = ConcessionnaireSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(
    tags=['Concessionnaires'],
    summary='Détails d\'un concessionnaire',
    description='Récupère les détails d\'un concessionnaire spécifique'
)
class ConcessionnaireDetailView(generics.RetrieveAPIView):
    """
    Récupère les détails d'un concessionnaire.
    
    GET : Retourne les détails d'un concessionnaire
    """
    queryset = Concessionnaire.objects.all()
    serializer_class = ConcessionnaireSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(
    tags=['Véhicules'],
    summary='Liste des véhicules d\'un concessionnaire',
    description='Récupère la liste de tous les véhicules d\'un concessionnaire spécifique'
)
class VehiculeListByConcessionnaireView(generics.ListAPIView):
    """
    Liste tous les véhicules d'un concessionnaire.
    
    GET : Retourne la liste de tous les véhicules d'un concessionnaire
    """
    serializer_class = VehiculeSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        concessionnaire_id = self.kwargs['concessionnaire_id']
        return Vehicule.objects.filter(concessionnaire_id=concessionnaire_id)


@extend_schema(
    tags=['Véhicules'],
    summary='Détails d\'un véhicule',
    description='Récupère les détails d\'un véhicule spécifique d\'un concessionnaire'
)
class VehiculeDetailView(generics.RetrieveAPIView):
    """
    Récupère les détails d'un véhicule.
    
    GET : Retourne les détails d'un véhicule
    """
    serializer_class = VehiculeSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        concessionnaire_id = self.kwargs['concessionnaire_id']
        return Vehicule.objects.filter(concessionnaire_id=concessionnaire_id)


@extend_schema(
    tags=['Authentification'],
    summary='Création d\'un utilisateur',
    description='Crée un nouvel utilisateur dans le système'
)
class UserCreateView(generics.CreateAPIView):
    """
    Crée un nouvel utilisateur.
    
    POST : Crée un nouvel utilisateur avec username, email et password
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'message': 'Utilisateur créé avec succès'
            },
            status=status.HTTP_201_CREATED
        )
