from django.conf import settings

import os
import google_apis_oauth
from django.shortcuts import HttpResponseRedirect, render
from googleapiclient.discovery import build


REDIRECT_URI = 'http://localhost:8000/google_oauth/callback/'
SCOPES = ['https://www.googleapis.com/auth/calendar']
JSON_FILEPATH = os.path.join(os.getcwd(), settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON)

def RedirectOauthView(request):
    oauth_url = google_apis_oauth.get_authorization_url(
        JSON_FILEPATH, SCOPES, REDIRECT_URI)
    return HttpResponseRedirect(oauth_url)


def CallbackView(request):
    credentials = google_apis_oauth.get_crendentials_from_callback(
        request,
        JSON_FILEPATH,
        SCOPES,
        REDIRECT_URI
    )   

    stringified_token = google_apis_oauth.stringify_credentials(
        credentials)
    creds = google_apis_oauth.load_credentials(stringified_token)
    service = build('calendar', 'v3', credentials=creds)
    return render(request, 'sucesso.html')