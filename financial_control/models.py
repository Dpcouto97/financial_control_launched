from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.urls import reverse
from django import template
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime


# Create your models here.
class TipoDespesa(models.Model):
    nome = models.CharField(max_length=50,blank=False, null=True)
    descricao = models.TextField(max_length=150,blank=False, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    user = models.IntegerField(blank=True, null=True) # Blank Significa que nao precisamos de introduzir valor manualmente!

    def __str__(self):
        return self.nome

    def get_detalhes_url(self):
        return reverse("tipodespesa-detalhes-view", kwargs={"my_id": self.id})

    def get_atualiza_url(self):
        return reverse("tipodespesa-atualiza-view", kwargs={"my_id": self.id})

    def get_elimina_url(self):
        return reverse("tipodespesa-elimina-view", kwargs={"my_id": self.id})

    def get_total_despesas_url(self):
        return reverse("tipodespesa-total-despesas-view", kwargs={"my_id": self.id})


class Despesa(models.Model):
    nome = models.CharField(max_length=50,blank=True, null=True)
    descricao = models.CharField(max_length=150,blank=True, null=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True)
    date = models.DateTimeField(blank=False, null=True)
    user = models.IntegerField(blank=True, null=True)
    tipo_despesa = models.ForeignKey(TipoDespesa, on_delete=models.SET_NULL, null=True)
    # on_delte=models.SET_NULL permite que possamos eliminar um tipo de despesa, sem as despesas serem eliminadas tmb em cascada, mas mesmo assim nao podemos deixar eliminar um tipo de despesa se tiver despesas associadas!

    def __str__(self):
        return self.nome

    def get_detalhes_url(self):
        return reverse("despesa-detalhes-view", kwargs={"my_id": self.id})

    def get_atualiza_url(self):
        return reverse("despesa-atualiza-view", kwargs={"my_id": self.id})

    def get_elimina_url(self):
        return reverse("despesa-elimina-view", kwargs={"my_id": self.id})


class Receita(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=300, blank=True, null=True)
    valor = models.FloatField(validators=[MaxValueValidator(1000000), MinValueValidator(0)], blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    user = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.nome