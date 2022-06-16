from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Despesa, TipoDespesa, Receita
from .forms import TipoDespesaRegistoForm


def tipodespesa_registo_view(request):
    form = TipoDespesaRegistoForm(request.POST or None)
    if form.is_valid():
        form.instance.user = request.user.id
        form.save()
        return HttpResponseRedirect(reverse('tipodespesa-lista-view'))
    else:
        print(form.errors)

    return render(request, "tipodespesa/tipodespesa_registo.html", {'form': form})


def tipodespesa_lista_view(request):
    tipodespesas = TipoDespesa.objects.filter(user=request.user.id)
    return render(request, "tipodespesa/tipodespesa_lista.html", {"tipodespesa_lista": tipodespesas})


def tipodespesa_detalhes_view(request, my_id):
    tipodespesa = get_object_or_404(TipoDespesa, id=my_id)
    return render(request, "tipodespesa/tipodespesa_detalhes.html", {"tipodespesa": tipodespesa})


def tipodespesa_atualiza_view(request, my_id):
    tipodespesa = get_object_or_404(TipoDespesa, id=my_id)
    form = TipoDespesaRegistoForm(request.POST or None, instance=tipodespesa)
    if form.is_valid():
        form.instance.user = request.user.id
        form.save()
        return HttpResponseRedirect(reverse('tipodespesa-lista-view'))
    return render(request, "tipodespesa/tipodespesa_atualiza.html", {'form': form, "tipodespesa": tipodespesa})


def tipodespesa_elimina_view(request, my_id):
    tipodespesa = get_object_or_404(TipoDespesa, id=my_id)
    tipodespesas = TipoDespesa.objects.filter(user=request.user.id)

    #Checka se o tipo de despesa tem despesas associadas, porque as depesas obrigatoriamente tem que ter um tipo de despesa!
    #Portanto a logica sera ter um botao para o utilizador escolher se realmente quer eliminar o tipo de despesa, informo
    #que todas as depesas associadas serao eliminadas! No maximo pode-se alterar as despesas para outro tipo de despesa e eliminar esse tipo de despesa.
    flag = False
    if len(tipodespesa.despesa_set.filter(user=request.user.id)) != 0:
        flag = True

    if request.method == "POST":
        tipodespesa.delete()
        return render(request, "tipodespesa/tipodespesa_lista_sucesso.html", {"tipodespesa_lista":tipodespesas})
    return render(request, "tipodespesa/tipodespesa_elimina.html", {"tipodespesa":tipodespesa, "flag": flag})


def tipodespesa_elimina_invalido_view(request, id_tipodespesa):
    despesas = Despesa.objects.filter(tipo_despesa=id_tipodespesa, user=request.user.id)
    tipodespesa = get_object_or_404(TipoDespesa, id=id_tipodespesa)
    return render(request, "tipodespesa/tipodespesa_elimina_listainvalido.html", {"despesa_lista": despesas, "tipodespesa":tipodespesa})


def tipodespesa_elimina_despesasetipo_view(request, id_tipodespesa):
    tipodespesa = get_object_or_404(TipoDespesa, id=id_tipodespesa)
    tipodespesas = TipoDespesa.objects.filter(user=request.user.id)
    despesas = Despesa.objects.filter(tipo_despesa=id_tipodespesa, user=request.user.id)

    # Elimina todas as despesas associadas a este tipo de despesa.
    for despesa in despesas:
        despesa.delete()

    # Elimina de seguida o tipo de despesa.
    tipodespesa.delete()

    return render(request, "tipodespesa/tipodespesa_lista_sucesso.html", {"tipodespesa_lista":tipodespesas})


def tipodespesa_elimina_guardaelimina_view(request, id_tipodespesa):
    tipodespesa = get_object_or_404(TipoDespesa, id=id_tipodespesa)
    despesas = Despesa.objects.filter(tipo_despesa=id_tipodespesa, user=request.user.id)
    return HttpResponseRedirect(reverse('tipodespesa-lista-view'))


def tipodespesa_total_despesas_view(request, my_id):
    tipodespesa = get_object_or_404(TipoDespesa, id=my_id)
    despesas = Despesa.objects.filter(tipo_despesa=my_id, user=request.user.id)

    total_custos = 0

    for despesa in despesas:
        total_custos += despesa.valor

    return render(request, "tipodespesa/tipodespesa_total_despesas.html", {"tipodespesa": tipodespesa, "total_custos": total_custos})