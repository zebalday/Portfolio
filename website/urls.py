from django.urls import path
from .views import *

app_name = 'website'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('home', IndexView.as_view(), name='home'),
    path('portfolio', Portfolio.as_view(), name='portfolio'),
    path('professional', ProfessionalInfo.as_view(), name='professional'),
    path('portfolio/projects/<int:id>', ProjectViewer.as_view(), name='project'),
]
