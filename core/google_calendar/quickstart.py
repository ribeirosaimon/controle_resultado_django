
from __future__ import print_function
import datetime
import pickle
import os.path


from django.conf import settings
from django.urls import reverse


SCOPES = "https://www.googleapis.com/auth/calendar"
REDIRECT_URL = 'http://127.0.0.1:8000/oauth2/calendar'
CLIENT_SECRETS_FILE = settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON

def create_google_calendar(request):

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES)
    flow.redirect_uri = reverse('oauth2callback')
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')

    # Store the state so the callback can verify the auth server response.
    flask.session['state'] = state
    print(authorization_url)
    return flask.redirect(authorization_url)

def authorize():
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON,
        scopes=['https://www.googleapis.com/auth/calendar'])
    flow.redirect_uri = 'http://127.0.0.1:8000/oauth2callback'
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')
    return authorization_url