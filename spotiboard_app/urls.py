from django.urls import path
from .views import *

app_name = "spotiboard_app"

urlpatterns = [
    path('redirect', spotify_callback, name='callback'),
    path('index', Index.as_view(), name='index'),
    path('dashboard', Dashboard.as_view(), name='dashboard'),
    path('tokens', AllTokens.as_view(), name='tokens'),
    path('tokens/<str:token>', AllTokens.as_view(), name='tokens'),
]
