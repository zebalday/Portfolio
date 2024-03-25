from .models import SpotifyToken
from django.utils import timezone
from datetime import timedelta
from requests import post, put, get
from .env_variables import *
from .serializers import SpotifyTokensSerializer



# Verify is there're saved tokens associated to an user session
def get_user_tokens(session_id):

    print(f"Get User Tokens | Session ID: {session_id}")

    try:
        user_tokens = SpotifyToken.objects.get(user=session_id)
        print(type(user_tokens))
        return user_tokens
    except:
        return None


# Create new tokens or update existing ones
def update_or_create_user_tokens(session_id, access_token, token_type, expires_in, refresh_token):
    
    tokens = get_user_tokens(session_id)

    #print(f"Valor que llega {expires_in}")
    #print(f"Hora actual {timezone.now()}")

    expires_in = timezone.now() + timedelta(seconds=expires_in)
    
    #print(f"Hora de expiración {expires_in}")
    
    # Update tokens
    if tokens:
        tokens.access_token = access_token
        tokens.refresh_token = refresh_token
        tokens.expires_in = expires_in
        tokens.token_type = token_type
        tokens.save(update_fields=['access_token', 'refresh_token', 'expires_in','token_type'])
        print("Acción Actualizar")

    # Create tokens
    else:
        tokens = SpotifyToken(user=session_id, access_token=access_token, refresh_token=refresh_token, token_type=token_type, expires_in=expires_in)
        tokens.save()
        print("Nueva Sesión Guardada")
        print(type(SpotifyToken.objects.get(user=session_id)))


# Check if user is authenticated (false if else) & its token hasn't expired (refresh if else)
def is_spotify_authenticated(session_id):
    
    tokens = get_user_tokens(session_id)
    #print(tokens)
    
    if tokens:
        expiry = tokens.expires_in
        if expiry <= timezone.now():
            refresh_spotify_token(session_id)
        return True
    return False


# Refresh spotify token
def refresh_spotify_token(session_id):
    
    refresh_token = get_user_tokens(session_id).refresh_token
    #print(refresh_token)

    response = post('https://accounts.spotify.com/api/token',
                    data = {
                        'grant_type':'refresh_token',
                        'refresh_token': refresh_token,
                        'client_id': CLIENT_ID,
                        'client_secret': CLIENT_SECRET
                        },
                    headers={
                        'Content-Type': 'application/x-www-form-urlencoded',
                        }
                    )
    
    #print(response.status_code)
    response = response.json()
    print(f"Refresh: {response}")

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    expires_in = response.get('expires_in')
    
    #print(refresh_token)

    try:
        update_or_create_user_tokens(session_id, access_token, token_type, expires_in, refresh_token)
    except Exception as ex:
        print(ex)


# Perform request to Spotify API endpoint
def execute_spotify_api_request(session_id, endpoint, post_=False, put_=False, params_={}):
    
    tokens = get_user_tokens(session_id)
    
    headers = {
        'Content-Type':'application/json',
        'Authorization': f'Bearer {tokens.access_token}'
    }
    
    if post_:
        post(BASE_URL + endpoint, headers = headers)
    
    if put_:
        put(BASE_URL + endpoint, headers = headers)
    
    
    response = get(BASE_URL + endpoint, headers=headers, params=params_)
    
    print(f"util: {response.status_code}")


    try:
        return response
    except:
        return ({'error':'Request error.'})