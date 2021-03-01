import os
import requests

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

from django.conf import settings
from django.urls import reverse
from django.shortcuts import redirect

CLIENT_SECRETS_FILE = settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON
SCOPES = ["https://www.googleapis.com/auth/calendar"]
API_SERVICE_NAME = 'calendar'
API_VERSION = 'v3'

def Authorize(request):
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES)
    flow.redirect_uri = request.build_absolute_uri(reverse('oauth2callback'))
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')
    request.session['state'] = state
    flow2 = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
    print(flow2)
    #https://developers.google.com/identity/protocols/oauth2/web-server
    return redirect(authorization_url)

def oauth2callback(request):
    
    state = request.session['state']
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
    redirect(flow.redirect_uri)

    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials
    request.session['credentials'] = credentials_to_dict(credentials)
    print(requests.session)

    return redirect('test_api_request')