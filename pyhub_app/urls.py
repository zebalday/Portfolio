from django.urls import path
from .views import *

app_name = "pyhub_app"

urlpatterns = [
    path("pyhub/app", pyhub_app.as_view(), name="pyhub-app")
]
