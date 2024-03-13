from django.shortcuts import render, redirect
from requests import Request, post
from django.views.generic import TemplateView
from .env_variables import *
from .util import *
from rest_framework import status
from datetime import datetime

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

    return redirect("spotiboard_app:dashboard")


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

        return render (request, self.template_name, self.context)


# The dashboard page to load user profile's info
class Dashboard(TemplateView):
    template_name = "spotiboard_app/dashboard.html"
    context= {}

    def get(self, request):
        
        self.context['is_auth'] = is_spotify_authenticated(request.session.session_key)
        self.context['user'] = get_user_info(request)
        self.context['current_song'] = get_current_song(request)
        self.context['songs_history'] = get_songs_history(request)
        #self.context['top_artists'], self.context['top_genres'] = get_top_artists_and_genres(request)
        #self.context['top_tracks'] = get_top_tracks(request)
        #self.context['last_saved_songs'] = get_last_saved_songs(request)
        #self.context['all_playlists'] = get_user_playlists(request)
        #self.context['followed_artists'] = get_user_followed_artists(request)


        return render(request, self.template_name, self.context)


""" METHODS FOR RETRIEVING INFO FROM SPOTIFY API"""
def get_user_info(request) -> dict:
    
    user_session = request.session.session_key
    endpoint = ""
    response = execute_spotify_api_request(user_session, endpoint)
    response = response.json()

    # Fetch info

    user_info = {
        'username': response.get('display_name'),
        'profile_url': response.get('external_urls').get('spotify'),
        'thumbnail': response.get('images')[-1].get('url'),
        'followers':response.get('followers').get('total')
    }

    return (user_info)

def get_songs_history(request) -> list:
    user_session = request.session.session_key
    endpoint = "/player/recently-played"
    response = execute_spotify_api_request(user_session, endpoint)
    response = response.json()
    
    track_list = []

    for track in response.get('items'):
        track_info = {
            'name': track.get('track').get('name'),
            'artists':get_all_artists(track.get('track').get('artists')),
            'album':track.get('track').get('album').get('name'),
            'thumbnail':track.get('track').get('album').get('images')[0].get('url'),
            'song_url':track.get('track').get('external_urls').get('spotify'),
        }
        track_list.append(track_info)
    
    return track_list

def get_current_song(request) -> dict:
    user_session = request.session.session_key
    endpoint = "/player/currently-playing"
    response = execute_spotify_api_request(user_session, endpoint)
    

    if response.status_code == 200:
        response = response.json()
        current_song = {
            'status':True,
            'name': response.get('item').get('name'),
            'artists':get_all_artists(response.get('item').get('artists')),
            'album':response.get('item').get('album').get('name'),
            'thumbnail':response.get('item').get('album').get('images')[0].get('url'),
            'song_url':response.get('item').get('external_urls').get('spotify'),
            'is_playing':response.get('is_playing')
        }
        return current_song
    
    elif response.status_code == 204:
        current_song = {'status':False}
        return current_song
    
    else:
        status = {'error':response}
        return status

def get_top_artists_and_genres(request) -> tuple:
    user_session = request.session.session_key
    endpoint = "/top/artists"
    response = execute_spotify_api_request(user_session, endpoint)
    response = response.json()

    artists_list = []
    all_genres = {}

    # Gettin artist info
    for artist in response.get('items'):
        artist = {
            'name':artist.get('name'),
            'artist_url':artist.get('external_urls').get('spotify'),
            'genres':artist.get('genres'),
            'thumbnail':artist.get('images')[0].get('url'),
            'followers':artist.get('followers').get('total'),
            'popularity':artist.get('popularity')
        }

        artists_list.append(artist)
        
        # Adding votes to each genre
        for genre in artist.get('genres'):
            if genre in all_genres:
                all_genres[genre] += 1
            else:
                all_genres[genre] = 1

        # Getting the top 10 genres in list format
        all_genres_sorted = sorted(all_genres.items(), key=lambda kv: kv[1], reverse=True)[:10]
        genres_list = [x[0] for x in all_genres_sorted]

    return (artists_list, genres_list)

def get_top_tracks(request) -> list:
    user_session = request.session.session_key
    endpoint = "/top/tracks"
    response = execute_spotify_api_request(user_session, endpoint)
    response = response.json()
    
    track_list = []

    for track in response.get('items'):
        track_info = {
            'name': track.get('name'),
            'artists':get_all_artists(track.get('artists')),
            'album':track.get('album').get('name'),
            'thumbnail':track.get('album').get('images')[0].get('url'),
            'song_url':track.get('external_urls').get('spotify'),
        }
        track_list.append(track_info)

    return track_list

def get_last_saved_songs(request) -> list:
    user_session = request.session.session_key
    endpoint = "/tracks"
    params = {'limit':10}
    response = execute_spotify_api_request(user_session, endpoint, params_=params)
    response = response.json()

    track_list = []
    for track in response.get('items'):

        track_info = {
            'name':track.get('track').get('name'),
            'added_at':get_formatted_date(track.get('added_at')),
            'artists':get_all_artists(track.get('track').get('artists')),
            'song_url':track.get('track').get('external_urls').get('spotify'),
        }

        track_list.append(track_info)
    
    return track_list

def get_user_playlists(request) -> list:
    user_session = request.session.session_key
    endpoint = "/playlists"
    params = {'limit':50, 'offset':0}

    response = execute_spotify_api_request(user_session, endpoint, params_=params)

    playlists = get_playlist_list(response.json())

    while params['offset'] <= response.json().get('total'):
        params['offset'] += 50
        response = execute_spotify_api_request(user_session, endpoint, params_=params)
        playlists += get_playlist_list(response.json())

    playlists = [p for p in playlists if p['name'] != ""]
    playlists_sorted = sorted(playlists, key=lambda kv: kv['total_songs'], reverse=True)

    return playlists_sorted

def get_user_followed_artists(request) -> list:
    user_session = request.session.session_key
    endpoint = "/following"
    params = {'type':'artist','limit':50}
    
    response = execute_spotify_api_request(user_session, endpoint, params_=params)
    response = response.json()
    
    followed_artists = get_followed_artists(response.get('artists').get('items'))

    params['after'] = response.get('artists').get('items')[-1].get('id')

    while len(followed_artists) < response.get('artists').get('total'):
        response = execute_spotify_api_request(user_session, endpoint, params_=params)
        response = response.json()
        followed_artists += get_followed_artists(response.get('artists').get('items'))
        params['after'] = response.get('artists').get('items')[-1].get('id')

    sorted_artists = sorted(followed_artists, key=lambda kv: kv["rank"], reverse=True)
    
    return sorted_artists

""" UTILS """
def get_all_artists(artists) -> list:
    artists_list = []

    for artist in artists:
        artist_info = {
            'name':artist.get('name'),
            'profile_url':artist.get('external_urls').get('spotify')
        }
        artists_list.append(artist_info)
    
    return artists_list

def get_formatted_date(date) -> str:
    date = datetime.strptime(date,"%Y-%m-%dT%H:%M:%SZ")
    return (date.strftime("%d-%m-%Y"))

def get_playlist_list(response) -> list:
    playlists = []

    for playlist in response.get('items'):
        playlist_info = {
            'name': playlist.get('name'),
            'total_songs':playlist.get('tracks').get('total'),
            'playlist_url':playlist.get('external_urls').get('spotify'),
            'owner':playlist.get('owner').get('display_name'),
            'owner_url':playlist.get('owner').get('external_urls').get('spotify'),
            'is_public':playlist.get('public'),
            'thumbnail':playlist.get('images')[0].get('url')
        }
        playlists.append(playlist_info)
    
    return playlists

def get_followed_artists(response) -> list:
    artists = []

    for artist in response:
        artist_info = {
            'name':artist.get('name'),
            'artist_url':artist.get('external_urls').get('spotify'),
            'followers':artist.get('followers').get('total'),
            'rank':artist.get('popularity'),
        }
        if len(artist.get('images')) > 0:
            artist_info['thumbnail'] = artist.get('images')[0].get('url')
        artists.append(artist_info)
    
    return artists