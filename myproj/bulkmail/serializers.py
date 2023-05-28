from django.contrib.auth.models import User, Group
from rest_framework import serializers

from rest_framework import serializers

class BulkEmailSerializer(serializers.Serializer):
    recipients = serializers.ListField(child=serializers.EmailField())
    subject = serializers.CharField()
    message = serializers.CharField()
