from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated, AllowAny
from rest_framework.generics import ListAPIView
from .serializers import *


# Create your views here.

class BulkMailView(views.APIView):
    permission_classes = [AllowAny,]
    serializer_class = BulkEmailSerializer

    def post(self, request, format=None):
        serializer = BulkEmailSerializer(data=request.data)
        if serializer.is_valid():
            recipients = serializer.validated_data['recipients']
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']

            send_mail(subject, message, 'exmp@g.com', recipients)
            return Response({'message': 'Bulk email is sent'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

