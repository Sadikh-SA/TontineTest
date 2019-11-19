from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class AdherentsAPIView(generics.ListCreateAPIView):
    queryset = adherents.objects.all()
    serializer_class = AdherentsSerializer

class CotisationAPIView(generics.ListCreateAPIView):
    queryset = cotisation.objects.all()
    serializer_class = CotisationSerializer


class NomTontineAPIView(generics.ListCreateAPIView):
    queryset = nomTontine.objects.all()
    serializer_class = NomTontineSerializer