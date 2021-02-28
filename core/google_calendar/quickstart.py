
from __future__ import print_function
import datetime
import pickle
import os.path

from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from allauth.socialaccount.models import SocialToken, SocialApp, SocialAccount

from django.conf import settings

SCOPES = "https://www.googleapis.com/auth/calendar"

def create_google_calendar(request):
    google_app = SocialApp.objects.get(provider='google')
    usuario = request.user

    user_account = SocialAccount.objects.get(user=request.user)
    user_token = user_account.socialtoken_set.first()

    client_key = google_app.client_id
    client_secret = google_app.secret
    resource_owner_key = user_token.token
    resource_owner_secret = user_token.token_secret


    auth = OAuth1Session(client_key, client_secret, resource_owner_key, resource_owner_secret)
    r = requests.get(protected_url, auth=auth)