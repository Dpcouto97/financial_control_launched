from django.contrib import admin
from .models import TipoDespesa, Despesa, Receita


# Register your models here.
admin.site.register(TipoDespesa)
admin.site.register(Despesa)
admin.site.register(Receita)