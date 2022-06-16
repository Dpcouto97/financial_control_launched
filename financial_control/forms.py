#The forms.py is where we should add the extra validations that we want to apply to the input forms income data/info
from django import forms
from django.core.exceptions import ValidationError
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Despesa, TipoDespesa, Receita


class TipoDespesaRegistoForm(forms.ModelForm):
    nome = forms.CharField(label=False, required=True)
    descricao = forms.CharField(label=False, widget=forms.Textarea(attrs={'name':'body', 'rows':3, 'cols':23}), required=True)
    user = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = TipoDespesa
        fields = [
            'nome',
            'descricao',
            'user'
        ]

    def clean_date(self):
        date = self.cleaned_data['date']
        if date > datetime.date.today():
            raise forms.ValidationError("The date must be the current day or before!")
        return date


class DespesaRegistoForm(forms.ModelForm):
    # Has to be forms.ModelForm, otherwise we cant use form.save() in the view
    nome = forms.CharField(label=False, required=True)
    descricao = forms.CharField(label=False, widget=forms.Textarea(attrs={'name':'body', 'rows':3, 'cols':23}), required=False)
    valor = forms.DecimalField(label=False, widget=forms.TextInput(attrs={"placeholder": "Formato: 2.00"}))
    user = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    tipo_despesa = forms.ModelChoiceField(queryset=TipoDespesa.objects.all(), label=False, required=True)
    date = forms.DateField(initial=datetime.date.today(), label=False, required=True)


    class Meta:
        model = Despesa
        fields = [
            'nome',
            'descricao',
            'valor',
            'user',
            'tipo_despesa',
            'date'
        ]

    def clean_date(self):
        date = self.cleaned_data['date']
        if date > datetime.date.today():
            raise forms.ValidationError("The date must be the current day or before!")
        return date


class ReceitaForm(forms.ModelForm):
    nome = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder": "Name"}), required=True)
    descricao = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder": "Description"}), required=True)

    class Meta:
        model = Receita
        fields = [
            'nome',
            'descricao'
        ]


class LoginForm(forms.Form):
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder": "Username"}), required=True)
    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={"placeholder": "Password"}), required=True)