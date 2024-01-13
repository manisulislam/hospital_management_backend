from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
# Create your views here.
# for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
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
            user=serializer.save()
            token=default_token_generator.make_token(user)
            print({"token":token})
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            print({"uid":uid})
            confirm_link=f"http://127.0.0.1:8000/patient/active/{uid}/{token}"
            email_subject="Confirmed Your Account"
            email_body=render_to_string("email_template.html",{"confirm_link":confirm_link})
            email=EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def activate(request, uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        user=User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user=None
        
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return redirect('register')
    else:
        return redirect('register')
    
class UserLogin(APIView):
   
    
    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']
            user=authenticate(username=username,password=password)
            if user:
                token , _ = Token.objects.get_or_create(user=user)
                return Response({"token":token.key}, status=status.HTTP_200_OK)
            else:
                return Response({"error":"Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            