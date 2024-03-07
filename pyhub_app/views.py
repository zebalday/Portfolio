from django.shortcuts import render, render
from django.views.generic import TemplateView
from .models import GithubUser
from .forms import GithubUserForm
from website.pyhub.GitHubAPI import GitHubApi
from .env_variables import *
from rest_framework import status
from datetime import datetime
import pytz



class Index(TemplateView):
    template_name = "pyhub_app/pyhub-index.html"
    api = GitHubApi(token=GITHUB_TOKEN)
    print(api.get_zen_info())

    def get(self, request):
        github_users = GithubUser.objects.all().values("username","url","thumbnail","last_consulted").distinct()
        user_form = GithubUserForm()

        context = {
            'users_list': github_users,
            'user_form': user_form,
        }
        print(type(github_users[0]['last_consulted']))
        return render(request, self.template_name, context)


    def post(self, request):

        if request.method == "POST":
            form = GithubUserForm(request.POST)
            
            if form.is_valid():
                username = form.cleaned_data['username']

                r_user = self.api.getUser(username)
                r_commits = self.api.getLastCommits(username, 10)
                r_followers = self.api.getUserFollowers(username)
                r_following = self.api.getUserFollowing(username)

                if r_user['status'] == status.HTTP_200_OK and r_commits['status'] == status.HTTP_200_OK and r_followers['status'] == status.HTTP_200_OK and r_following['status'] == status.HTTP_200_OK:
                    
                    # Check if user is already in the database
                    if GithubUser.objects.get(username=username):
                        user_update = GithubUser.objects.get(username=username)
                        
                        user_update.last_consulted = datetime.now()
                        
                        user_update.thumbnail = r_user['user']['avatar_url']
                        user_update.save()

                    else:
                        new_user = GithubUser(username=username, url=r_user['user']['user_url'], thumbnail=r_user['user']['avatar_url'])
                        new_user.save()
                    
                    context = {
                        'github_user':r_user['user'],
                        'github_commits':r_commits['commits'],
                        'github_followers':r_followers['followers'],
                        'github_following':r_following['following']
                    }
                    return render(request, self.template_name, context)
                else:
                    print(r_user)
                    print(r_commits)
                    print(r_followers)
                    print(r_following)
                    context = {'petition_error':"Error"}
                
                return render(request, self.template_name, context)