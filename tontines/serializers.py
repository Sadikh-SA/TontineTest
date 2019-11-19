from rest_framework import serializers
from .models import *

class AdherentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = adherents
        fields = "__all__"

class CotisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = cotisation
        fields = "__all__"

class NomTontineSerializer(serializers.ModelSerializer):
    class Meta:
        model = nomTontine
        fields = "__all__"
