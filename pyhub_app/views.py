from django.shortcuts import render, render
from django.views.generic import TemplateView
from .models import GithubUser
from .forms import GithubUserForm
from website.pyhub.GitHubAPI import GitHubApi
from .env_variables import *


class pyhub_app(TemplateView):
    template_name = "pyhub_app/pyhub_index.html"
    context = {}
    api = GitHubApi(token=GITHUB_TOKEN)

    def get(self, request):
        #github_users = GithubUser.objects.all()

        github_user = self.api.getUser("zebalday")
        github_commits = self.api.getLastCommits("zebalday", 10)

        if github_user.status_code == 200 and github_commits.status_code == 200:
            print (github_user.data)
            print (github_commits.data)

        #self.context['users']
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = GithubUserForm(request.POST)
        
        if form.is_valid():
            form = form.cleaned_data()
            username = form['username']
            github_user = self.api.getUser(username)
            github_commits = self.api.getLastCommits(username)

            #if github_user.status_code == 200


        pass
