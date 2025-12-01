from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Concessionnaire, Vehicule


class UserSerializer(serializers.ModelSerializer):
    """Serializer pour les utilisateurs"""
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user


class VehiculeSerializer(serializers.ModelSerializer):
    """Serializer pour les véhicules - inclut tous les champs"""
    class Meta:
        model = Vehicule
        fields = ['id', 'type', 'marque', 'chevaux', 'prix_ht', 'concessionnaire']
        read_only_fields = ['id']


class ConcessionnaireSerializer(serializers.ModelSerializer):
    """Serializer pour les concessionnaires - exclut le champ siret"""
    vehicules = VehiculeSerializer(many=True, read_only=True)
    
    class Meta:
        model = Concessionnaire
        fields = ['id', 'nom', 'vehicules']
        read_only_fields = ['id', 'vehicules']
    
    def to_representation(self, instance):
        """S'assure que siret n'est jamais exposé"""
        representation = super().to_representation(instance)
        # Siret est déjà exclu des fields, mais on s'assure qu'il n'apparaît pas
        representation.pop('siret', None)
        return representation
