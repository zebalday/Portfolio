from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Project
from .forms import UserForm

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"
    featured_projects = Project.objects.all()
    context = {
        'featured_projects' : featured_projects,
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


