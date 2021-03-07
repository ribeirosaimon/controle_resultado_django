from django.conf import settings

import os
import google_apis_oauth
from django.shortcuts import HttpResponseRedirect, render
from googleapiclient.discovery import build
from urllib.parse import urlencode
from core.google_calendar.criar_eventos import *
from django.contrib.sites.models import Site


SCOPES = ['https://www.googleapis.com/auth/calendar']
JSON_FILEPATH = os.path.join(os.getcwd(), settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON)

def RedirectOauthView(request):
    current_site = Site.objects.get_current()
    REDIRECT_URI = f'https://{current_site.domain}/google_oauth/callback/'
    oauth_url = google_apis_oauth.get_authorization_url(
        JSON_FILEPATH, SCOPES, REDIRECT_URI)
    return HttpResponseRedirect(oauth_url)


def CallbackView(request):
    REDIRECT_URI = f'https://{current_site.domain}/google_oauth/callback/'
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
    criar_eventos(service, settings.DICT_SERVICE['empresas'])
    return render(request, 'sucesso.html')