from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.

class SpecializationViewSets(viewsets.ModelViewSet):
    queryset=models.Specialization.objects.all()
    serializer_class=serializers.SpecializationSerializer

class DesignationViewSets(viewsets.ModelViewSet):
    queryset=models.Designation.objects.all()
    serializer_class=serializers.DesignationSerializer

class AvailableTimeViewSets(viewsets.ModelViewSet):
    queryset=models.AvailableTime.objects.all()
    serializer_class=serializers.AvailableTimeSerializer

class DoctorViewSets(viewsets.ModelViewSet):
    queryset=models.Doctor.objects.all()
    serializer_class=serializers.DoctorSerializer

class ReviewViewSets(viewsets.ModelViewSet):
    queryset=models.Review.objects.all()
    serializer_class=serializers.ReviewSerializer