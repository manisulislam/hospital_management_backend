from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
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
    
class RegistrationApiView(APIView):
    serializer_class=serializers.RegistrationSerializer
    
    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)