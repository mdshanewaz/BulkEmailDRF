from django.urls import path

from .views import *

urlpatterns = [
    path("", BulkMailView.as_view()),
]