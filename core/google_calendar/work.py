from allauth.socialaccount.models import SocialAccount, SocialApp
import requests
from requests_oauthlib import OAuth1Session

def credencial(request):
    google_app = SocialApp.objects.get(provider='google')
    usuario = request.user
    print(usuario, '---------------')
    user_account = SocialAccount.objects.get(user=request.user)
    user_token = user_account.socialtoken_set.first()

    client_key = google_app.client_id
    client_secret = google_app.secret
    resource_owner_key = user_token.token
    resource_owner_secret = user_token.token_secret


    auth = OAuth1Session(client_key, client_secret, resource_owner_key, resource_owner_secret)
    r = requests.get(protected_url, auth=auth)
    print(r)