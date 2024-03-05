from django.shortcuts import render, render
from django.views.generic import TemplateView
from .models import GithubUser
from .forms import GithubUserForm
from website.pyhub.GitHubAPI import GitHubApi
from .env_variables import *
from rest_framework import status


class pyhub_app(TemplateView):
    template_name = "pyhub_app/pyhub_index.html"
    api = GitHubApi(token=GITHUB_TOKEN)


    def get(self, request):
        github_users = GithubUser.objects.all().values("username").distinct()
        user_form = GithubUserForm()

        context = {
            'users_list': github_users,
            'user_form': user_form,
        }

        return render(request, self.template_name, context)


    def post(self, request):
        form = GithubUserForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']

            r_user = self.api.getUser(username)
            r_commits = self.api.getLastCommits(username, 10)
            r_followers = self.api.getUserFollowers(username)
            r_following = self.api.getUserFollowing(username)

            if r_user['status'] == status.HTTP_200_OK and r_commits['status'] == status.HTTP_200_OK and r_followers['status'] == status.HTTP_200_OK and r_following['status'] == status.HTTP_200_OK:
                context = {
                    'github_user':r_user['user'],
                    'github_commits':r_commits['commits'],
                    'github_followers':r_followers['followers'],
                    'github_following':r_following['following']
                }
                new_user = GithubUser(username=username, url=r_user['user']['user_url'], thumbnail=r_user['user']['avatar_url'])
                new_user.save()
            else:
                context = {'petition_error':"Error"}
            
            return render(request, self.template_name, context)


