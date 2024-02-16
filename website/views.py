from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Project

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"
    featured_projects = Project.objects.all()
    context = {
        'featured_projects' : featured_projects,
    }

    def get(self, request):
        return render(request, self.template_name, self.context)



