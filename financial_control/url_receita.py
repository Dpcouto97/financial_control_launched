from django.urls import path
from .view_despesa import despesa_register_view, despesa_details_view, despesa_list_view, despesa_edit_view, client_update_view, client_delete_view

urlpatterns = [
    path('registo/', client_register_view, name='client-register-view'),
    path('lista/', client_list_view, name='client-list-view'),
    path('detalhes/<int:my_id>/', client_details_view, name='client-details-view'),
    path('atualizar/<int:my_id>/', client_update_view, name='client-update-view'),
    path('eliminar/<int:my_id>/', client_delete_view, name='client-delete-view'),
]