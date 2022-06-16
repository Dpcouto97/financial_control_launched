from django.urls import path
from .view_tipodespesa import tipodespesa_registo_view, tipodespesa_lista_view, tipodespesa_detalhes_view, tipodespesa_elimina_view, tipodespesa_atualiza_view, tipodespesa_total_despesas_view, tipodespesa_elimina_invalido_view,\
    tipodespesa_elimina_despesasetipo_view, tipodespesa_elimina_guardaelimina_view

urlpatterns = [
    path('registo/', tipodespesa_registo_view, name='tipodespesa-registo-view'),
    path('lista/', tipodespesa_lista_view, name='tipodespesa-lista-view'),
    path('detalhes/<int:my_id>/', tipodespesa_detalhes_view, name='tipodespesa-detalhes-view'),
    path('atualizar/<int:my_id>/', tipodespesa_atualiza_view, name='tipodespesa-atualiza-view'),
    path('eliminar/<int:my_id>/', tipodespesa_elimina_view, name='tipodespesa-elimina-view'),
    path('eliminar/invalido/listadespesas/<int:id_tipodespesa>/', tipodespesa_elimina_invalido_view, name='tipodespesa-elimina-invalido-view'),
    path('eliminar/invalido/despesasetipo/<int:id_tipodespesa>/', tipodespesa_elimina_despesasetipo_view, name='tipodespesa-elimina-despesasetipo-view'),
   # path('eliminar/invalido/guardaelimina/<int:id_tipodespesa>/', tipodespesa_elimina_guardaelimina_view, name='tipodespesa-elimina-guardaelimina-view'),
    path('totaldespesa/<int:my_id>/', tipodespesa_total_despesas_view, name='tipodespesa-total-despesas-view'),
]