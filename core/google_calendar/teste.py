from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from allauth.socialaccount.models import SocialToken, SocialApp, SocialAccount


import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleads import oauth2
from oauth2client.client import flow_from_clientsecrets
from requests_oauthlib import OAuth2Session





def create_google_calendar(request):
    authorize()
    google_app = SocialApp.objects.get(provider='google')
    usuario = request.user

    user_account = SocialAccount.objects.get(user=request.user)
    user_token = user_account.socialtoken_set.first()
    client_key = google_app.client_id
    client_secret = google_app.secret
    resource_owner_key = user_token.token
    resource_owner_secret = user_token.token_secret

    #https://www.youtube.com/watch?v=kj9llVn5vJI
