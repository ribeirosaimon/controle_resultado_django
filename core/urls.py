from django.urls import path
from .views import ResultadoViews, IndexView, SucessoViews
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from .views_google import RedirectOauthView, CallbackView


urlpatterns = [
    path('',IndexView.as_view(template_name="index.html"), name='index'),
    path('resultados',ResultadoViews.as_view(), name='resultados'),
    path('sucesso',SucessoViews.as_view(), name='sucesso'),
    #path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
    path('google_oauth/redirect/', RedirectOauthView),
	path('google_oauth/callback/', CallbackView)
]