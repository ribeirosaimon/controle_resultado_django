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

def create_google_calendar(request):
    token = SocialToken.objects.get(account__user=request.user, account__provider='google')
    google_app = SocialApp.objects.get(provider='google')
    social_info = SocialAccount.objects.filter(user=request.user)
    credentials = Credentials(
            token=token.token,
            token_uri="https://www.googleapis.com/oauth2/v3/token", 
            client_id=google_app.client_id,
            client_secret=google_app.secret,
        )
    service = build('calendar', 'v3', credentials=credentials)
    return service