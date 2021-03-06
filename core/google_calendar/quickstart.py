from django.views.generic import TemplateView
from google_auth_oauthlib import flow
from django.conf import settings
from googleapiclient.discovery import build


def authorize():
    launch_browser = True
    appflow = flow.InstalledAppFlow.from_client_secrets_file(
        settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON, scopes=["https://www.googleapis.com/auth/calendar"]
    )
    if launch_browser:
        appflow.run_local_server()
    else:
        appflow.run_console()
    credentials = appflow.credentials
    service = build('calendar', 'v3', credentials=credentials)
    return service