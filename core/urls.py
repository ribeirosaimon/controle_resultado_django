from django.urls import path
from .views import ResultadoViews, IndexView, SucessoViews
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('',IndexView.as_view(template_name="index.html"), name='index'),
    path('resultados',ResultadoViews.as_view(), name='resultados'),
    path('sucesso',SucessoViews.as_view(), name='sucesso'),
    #https://stackoverflow.com/questions/62097219/getting-a-error-400-redirect-uri-mismatch-when-trying-to-use-oauth2-with-google
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),)
]