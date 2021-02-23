from .criar_eventos import *
import os

def conferir_google_com_b3(service, empresas):
    page_token = None
    while True:
        events = service.events().list(calendarId='primary', pageToken=page_token).execute()
        for event in events['items']:
            deletar_evento(service, event['id'])
        page_token = events.get('nextPageToken')
        if not page_token:
            break
    criar_eventos(service, empresas)
    os.remove('token.pickle')
