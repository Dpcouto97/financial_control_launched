from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Despesa, TipoDespesa, Receita
from .forms import DespesaRegistoForm
from datetime import datetime, timedelta

def despesa_registo_view(request):
    tipodespesa = TipoDespesa.objects.filter(user=request.user.id)
    if not tipodespesa:
        return render(request, "despesa/despesa_registo_invalido.html")

    form = DespesaRegistoForm(request.POST or None)
    if form.is_valid():
        form.instance.user = request.user.id
        form.save()
        return HttpResponseRedirect(reverse('despesa-lista-view'))
    else:
        print(form.errors)

    return render(request, "despesa/despesa_registo.html", {'form': form})


def despesa_lista_view(request):
    despesas = Despesa.objects.filter(user=request.user.id)
    return render(request, "despesa/despesa_lista.html", {"despesa_lista": despesas})


def despesa_detalhes_view(request, my_id):
    despesa = get_object_or_404(Despesa, id=my_id)
    return render(request, "despesa/despesa_detalhes.html", {"despesa": despesa})


def despesa_atualiza_view(request, my_id):
    despesa = get_object_or_404(Despesa, id=my_id)
    form = DespesaRegistoForm(request.POST or None, instance=despesa)
    if form.is_valid():
        form.instance.user = request.user.id
        form.save()
        return HttpResponseRedirect(reverse('despesa-lista-view'))
    return render(request, "despesa/despesa_atualiza.html", {'form': form, "despesa": despesa})


def despesa_elimina_view(request, my_id):
    despesa = get_object_or_404(Despesa, id=my_id)

    if request.method == "POST":
        despesa.delete()
        return HttpResponseRedirect(reverse('despesa-lista-view'))
    return render(request, "despesa/despesa_elimina.html", {"despesa":despesa})


def despesa_visaogeral_view(request):
    despesas = Despesa.objects.filter(user=request.user.id)

    today = datetime.today()
    yesterday = today - timedelta(days=1)
    one_week_ago = today - timedelta(days=7)
    thirty_days_ago = today - timedelta(days=30)
    six_months_ago = today - timedelta(days=182)
    one_year_ago = today - timedelta(days=365)

    print(one_week_ago )
    print(thirty_days_ago)
    print(six_months_ago)

    despesas_7dias = []
    despesas_7dias_total = 0
    # Despesas dos ultimos 7 Dias
    for despesa in despesas:
        if despesa.date >= one_week_ago:
            despesas_7dias.append(despesa)
            despesas_7dias_total += despesa.valor

    despesas_30dias = []
    despesas_30dias_total = 0
    # Despesas dos ultimos 30 Dias
    for despesa in despesas:
        if despesa.date >= thirty_days_ago:
            despesas_30dias.append(despesa)
            despesas_30dias_total += despesa.valor

    despesas_6meses = []
    despesas_6meses_total = 0
    # Despesas dos ultimos 6 Meses
    for despesa in despesas:
        if despesa.date >= six_months_ago :
            despesas_6meses.append(despesa)
            despesas_6meses_total += despesa.valor

    despesas_1ano = []
    despesas_1ano_total = 0
    # Despesas dos ultimos 6 Meses
    for despesa in despesas:
        if despesa.date >= one_year_ago:
            despesas_1ano.append(despesa)
            despesas_1ano_total += despesa.valor

    return render(request, "despesa/despesa_visaogeral.html", {"despesas_7dias_total": despesas_7dias_total,"despesas_30dias_total": despesas_30dias_total,"despesas_6meses_total": despesas_6meses_total,"despesas_1ano_total": despesas_1ano_total})

def despesa_7dias_lista_view(request):
    despesas = Despesa.objects.filter(user=request.user.id)

    today = datetime.today()
    one_week_ago = today - timedelta(days=7)

    despesas_7dias = []
    despesas_7dias_total = 0
    # Despesas dos ultimos 7 Dias
    for despesa in despesas:
        if despesa.date >= one_week_ago:
            despesas_7dias.append(despesa)
            despesas_7dias_total += despesa.valor
    return render(request, "despesa/despesa_visaogeral_7dias.html", {"despesas_7dias_lista": despesas_7dias,"despesas_7dias_total": despesas_7dias_total})


def despesa_30dias_lista_view(request):
    despesas = Despesa.objects.filter(user=request.user.id)

    today = datetime.today()
    thirty_days_ago = today - timedelta(days=30)

    despesas_30dias = []
    despesas_30dias_total = 0
    # Despesas dos ultimos 7 Dias
    for despesa in despesas:
        if despesa.date >= thirty_days_ago:
            despesas_30dias.append(despesa)
            despesas_30dias_total += despesa.valor
    return render(request, "despesa/despesa_visaogeral_30dias.html", {"despesas_30dias_lista": despesas_30dias,"despesas_30dias_total": despesas_30dias_total})


def despesa_6meses_lista_view(request):
    despesas = Despesa.objects.filter(user=request.user.id)

    today = datetime.today()
    six_months_ago = today - timedelta(days=182)

    despesas_6meses = []
    despesas_6meses_total = 0
    # Despesas dos ultimos 7 Dias
    for despesa in despesas:
        if despesa.date >= six_months_ago :
            despesas_6meses.append(despesa)
            despesas_6meses_total += despesa.valor
    return render(request, "despesa/despesa_visaogeral_6meses.html", {"despesas_6meses_lista": despesas_6meses,"despesas_6meses_total": despesas_6meses_total})


def despesa_1ano_lista_view(request):
    despesas = Despesa.objects.filter(user=request.user.id)

    today = datetime.today()
    one_year_ago = today - timedelta(days=365)

    despesas_1ano = []
    despesas_1ano_total = 0
    # Despesas dos ultimos 7 Dias
    for despesa in despesas:
        if despesa.date >= one_year_ago:
            despesas_1ano.append(despesa)
            despesas_1ano_total += despesa.valor
    return render(request, "despesa/despesa_visaogeral_1ano.html", {"despesas_1ano_lista": despesas_1ano,"despesas_1ano_total": despesas_1ano_total})