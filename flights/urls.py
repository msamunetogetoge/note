from django.urls import path
import os
from . import views
from pathlib import Path

app_name="flights"
urlpatterns=[
    path("", views.index, name="index"),
    path("with_model", views.form_with_model, name="with_model"),
    path("without_model", views.form_without_model, name="without_model")
    
]

