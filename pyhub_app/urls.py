from django.urls import path
from .views import *

app_name = "pyhub_app"

urlpatterns = [
    path("index", Index.as_view(), name="index")
]
