from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.

class PatientViewSets(viewsets.ModelViewSet):
    queryset=models.Patient.objects.all()
    serializer_class=serializers.PatientSerializer
    
    def get_queryset(self):
        queryset=super().get_queryset()
        patient_id=self.request.query_params.get('patient_id')
        if patient_id is not None:
            queryset=queryset.filter(patient_id=patient_id)
        return queryset