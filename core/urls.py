from django.urls import path
from .views import ResultadoViews, IndexView
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('',IndexView.as_view(template_name="index.html"), name='index'),
    path('resultados',ResultadoViews.as_view(), name='resultados'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),)
]