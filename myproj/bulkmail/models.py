from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Create your models here.

class BulkMail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipients = ArrayField(models.EmailField(max_length=1000), blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.user


    