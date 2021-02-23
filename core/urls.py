from django.urls import path
from .views import ResultadoViews

urlpatterns = [
    path('',ResultadoViews.as_view(), name='resultados')
]