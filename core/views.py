from django.shortcuts import render
from django.views.generic.base import View
from django.urls import reverse_lazy
from .service import open_csv


class ResultadoViews(View):
    def get(self, request, *args, **kwargs):
        context = {'info':open_csv()}
        return render(request, "resultados.html", context=context)
    def post(self,request, *args, **kwargs):
        empresas = request.POST.getlist('empresas')
        return render(request, "resultados.html")