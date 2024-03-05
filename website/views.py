from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Project, ProjectImage
from .pyhub.GitHubAPI import GitHubApi
from .env_variables import *
from rest_framework import status


# HOME SCREEN - LANDING PAGE
class IndexView(TemplateView):
    template_name = "website/index.html"

    def get(self, request):
        
        if not request.session.exists(request.session.session_key):
            request.session.create()

        return render(request, self.template_name)


# ABOUT ME - PROFESSIONAL INFORMATION PAGE
class ProfessionalInfo(TemplateView):
    
    template_name = "website/professional-info.html"
    context = {}

    def get(self, request):

        """ api = GitHubApi(token=GITHUB_TOKEN)
        github_user = api.getUser("zebalday")
        github_commits = api.getLastCommits("zebalday", 5)


        if github_user['status'] == status.HTTP_200_OK and github_commits['status'] == status.HTTP_200_OK:
            self.context = {
                "github_user" : github_user['user'],
                "github_commits" : github_commits['commits']
        } """

        return render(request, self.template_name, self.context)


# GITHUB ACTIVITY
class GithubActivity(TemplateView):
    template_name = "website/github-activity.html"
    context = {}

    def get(self, request):

        if (('github_user' not in request.session) or ('github_commits' not in request.session)):
            
            api = GitHubApi(token=GITHUB_TOKEN)
            github_user = api.getUser("zebalday")
            github_commits = api.getLastCommits("zebalday", 5)

            if github_user['status'] == status.HTTP_200_OK and github_commits['status'] == status.HTTP_200_OK:
                self.context = {
                    "github_user" : github_user['user'],
                    "github_commits" : github_commits['commits']
                }

                request.session["github_user"] = github_user['user']
                request.session["github_commits"] = github_commits['commits']

                return render(request, self.template_name, self.context)
            
            self.context['error': status.HTTP_400_BAD_REQUEST]
            
            return render(request, self.template_name, self.context)
        
        self.context = {
                "github_user" : request.session["github_user"],
                "github_commits" : request.session["github_commits"]
        }

        return render(request, self.template_name, self.context)


# PORTFOLIO - PROJECTS LISTING
class Portfolio(TemplateView):
    template_name = "website/portfolio.html"

    # >> Send public projects through context processor (get_public_projects)

    def get(self, request):
        return render(request, self.template_name)


# SINGLE PROJECT PAGE
class ProjectViewer(TemplateView):
    template_name = "website/project-viewer.html"
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
