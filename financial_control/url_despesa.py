from django.urls import path
from .view_despesa import despesa_registo_view, despesa_detalhes_view, despesa_lista_view, despesa_atualiza_view, despesa_elimina_view, despesa_visaogeral_view, despesa_7dias_lista_view, despesa_30dias_lista_view, \
    despesa_6meses_lista_view, despesa_1ano_lista_view

urlpatterns = [
    path('registo/', despesa_registo_view, name='despesa-registo-view'),
    path('lista/', despesa_lista_view, name='despesa-lista-view'),
    path('detalhes/<int:my_id>/', despesa_detalhes_view, name='despesa-detalhes-view'),
    path('atualizar/<int:my_id>/', despesa_atualiza_view, name='despesa-atualiza-view'),
    path('eliminar/<int:my_id>/', despesa_elimina_view, name='despesa-elimina-view'),
    path('visaogeral/', despesa_visaogeral_view, name='despesa-visaogeral-view'),
    path('visaogeral/despesas/7dias/', despesa_7dias_lista_view, name='despesa-7dias-lista-view'),
    path('visaogeral/despesas/30dias/', despesa_30dias_lista_view, name='despesa-30dias-lista-view'),
    path('visaogeral/despesas/6meses/', despesa_6meses_lista_view, name='despesa-6meses-lista-view'),
    path('visaogeral/despesas/1ano/', despesa_1ano_lista_view, name='despesa-1ano-lista-view'),
]