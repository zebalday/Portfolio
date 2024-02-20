from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Project, User, Language, Framework, Library
from .forms import UserForm

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)


class Portfolio(TemplateView):
    template_name = "portfolio.html"

    projects = Project.objects.filter(is_public=True)
    projects_full_info_list = []

    # Relate project with its languages and framewworks
    for project in projects:
        related_languages = project.languages.all()
        related_frameworks = project.framework.all()
        related_libraries = project.libraries.all()

        if related_libraries.filter(name__in=("Pandas","Numpy","Seaborn","MatPlotLib")).exists():
            filter_identifier = "filter-datascience"
        elif related_frameworks.filter(name="Django").exists():
            filter_identifier = "filter-django"
        elif related_languages.filter(name="Python").exists():
            filter_identifier = "filter-python"
        else:
            filter_identifier = ""

        # Create dictionary with project and its tags
        full_project = {"project":project,
                        "languages":related_languages,
                        "framework":related_frameworks,
                        "libraries":related_libraries,
                        "filter":filter_identifier,
                        }
        
        # Add dictionary to the list of projects
        projects_full_info_list.append(full_project)

    context = {
        "projects_full":projects_full_info_list,
    }

    def get(self, request):
        return render(request, self.template_name, self.context)



class RegisterUser(TemplateView):
    template_name = "register.html"
    user_form = UserForm
    context = {
        'user_form' : user_form,
    }

    def get(self, request):
        return render(request, self.template_name, self.context)


class Login(TemplateView):
    template_name = "login.html"
    user_form = UserForm
    context = {
        'user_form' : user_form,
    }

    def get(self, request):
        return render(request, self.template_name, self.context)


