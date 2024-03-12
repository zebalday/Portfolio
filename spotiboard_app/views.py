from django.shortcuts import render, redirect
from requests import Request, post
from django.views.generic import TemplateView
from .env_variables import *
from .util import *

# Prepares the authentication URL for spotify app
def get_auth_url():
    scope = """
                    playlist-read-collaborative
                    playlist-read-private
                    user-follow-read
                    user-library-read
                    user-read-currently-playing
                    user-read-playback-state
                    user-read-recently-played
                    user-top-read
                """
    scope = scope.strip()

    url = Request(
        'GET', 'https://accounts.spotify.com/authorize',
            params={
                'scope': scope,
                'response_type': 'code',
                'redirect_uri': REDIRECT_URI,
                'client_id': CLIENT_ID,
            }
    ).prepare().url

    return url

# Callback from spotify to the server. Returns the token info.
def spotify_callback(request):

    code = request.GET.get('code')
    error = request.GET.get('error')

    # Performing post petition
    response = post(
                'https://accounts.spotify.com/api/token',
                data = {
                    'grant_type' : 'authorization_code',
                    'code' : code,
                    'redirect_uri' : REDIRECT_URI,
                    'client_id': CLIENT_ID,
                    'client_secret': CLIENT_SECRET,
                }
            ).json()

    # Fetching data from response
    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')
    error = response.get('error')

    # Verify if there's an active user session
    if not request.session.exists(request.session.session_key):
        request.session.create()

    # Saving tokens on the database
    update_or_create_user_tokens(request.session.session_key, access_token=access_token, token_type=token_type, expires_in=expires_in, refresh_token=refresh_token)

    return redirect("spotiboard_app:index")


# TESTS
""" def layout(request):
    return render(request, template_name='spotiboard_app/layout.html') """


# The login page
class Index(TemplateView):

    template_name = "spotiboard_app/index.html"
    auth_url = get_auth_url()

    context = {
        'auth_url':auth_url,
    }

    def get(self, request):

        self.context['is_auth'] = is_spotify_authenticated(request.session.session_key)
        return render (request, self.template_name, self.context)


# The dashboard page to load user profile's info
class Dashboard(TemplateView):
    template_name = "spotiboard_app/dashboard.html"
    context= {}

    def get(self, request):
        return render(request, self.template_name, self.context)

