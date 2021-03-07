from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .service import open_csv
from core.google_calendar.quickstart import *
from core.google_calendar.criar_eventos import *
from core.google_calendar.conferir_calendario import *
from django.contrib import messages
import os
from urllib.parse import urlencode
from django.contrib.sites.models import Site


class ResultadoViews(View):
    def get(self, request, *args, **kwargs):
        context = {'info':open_csv()}
        return render(request, "resultados.html", context=context)
    def post(self,request, *args, **kwargs):
        empresas = request.POST.getlist('empresas')
        settings.DICT_SERVICE['empresas'] = empresas
        current_site = Site.objects.get_current()
        URL = f'{settings.DOMINIO_ABSOLUTO}/google_oauth/redirect/'
        return HttpResponseRedirect(URL)



class IndexView(TemplateView):
    template_name = 'index.html'

class SucessoViews(TemplateView):   
    template_name = 'sucesso.html'


