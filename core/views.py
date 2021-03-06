from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .service import open_csv
from core.google_calendar.quickstart import *
from core.google_calendar.criar_eventos import *
from core.google_calendar.conferir_calendario import *
from django.contrib import messages
import os

from core.google_calendar.to_do import *


class ResultadoViews(View):
    def get(self, request, *args, **kwargs):
        context = {'info':open_csv()}
        return render(request, "resultados.html", context=context)
    def post(self,request, *args, **kwargs):
        try:
            os.remove('token.pickle')
        except:
            pass
        empresas = request.POST.getlist('empresas')
        authorize()

        #service = create_google_calendar(request)
        #criar_eventos(service, empresas)

        return render(request, "sucesso.html")


class IndexView(TemplateView):
    template_name = 'index.html'

class SucessoViews(TemplateView):   
    template_name = 'sucesso.html'