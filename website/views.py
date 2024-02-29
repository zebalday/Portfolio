from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Project, ProjectImage, User, Language, Framework, Library
from .pyhub.GitHubAPI import GitHubApi


# HOME SCREEN - LANDING PAGE
class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)

# PROFESSIONAL INFORMATION PAGE
class ProfessionalInfo(TemplateView):
    
    template_name = "professional-info.html"
    context = {}

    api = GitHubApi(token="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")
    print(api)
    print(api.get_zen_info())

    github_user = api.getUser("zebalday")
    github_last_commits = api.getLastCommits("zebalday", 5)

    context = {
        "github_user" : github_user,
        "github_commits" : github_last_commits
    }

    def get(self, request):
        return render(request, self.template_name, self.context)


# PROJECTS RELATED
class Portfolio(TemplateView):
    template_name = "portfolio.html"

    # >> Send public projects through context processor (get_public_projects)

    def get(self, request):
        return render(request, self.template_name)

class ProjectViewer(TemplateView):
    template_name = "project-viewer.html"
    context = {}
    
    def get(self, request, id):

        # Empty list
        projects_full_info_list = []

        # Get Project from DB
        project = Project.objects.get(id=id)

        # Get related technologies from DB
        languages = project.languages.all()
        framework = project.framework.all()
        libraries = project.libraries.all()

        # Get project images from DB
        project_images = ProjectImage.objects.filter(project_id=id)

        # Create dictionary with project and its tags
        full_project = {"project":project,
                        "languages":languages,
                        "framework":framework,
                        "libraries":libraries,
                        "project_images":project_images
                        }

        # Send info to context
        projects_full_info_list.append(full_project)
        self.context["projects_full"] = projects_full_info_list

        # Render view
        return render(request, self.template_name, self.context)

    def post(self, request):
        pass
