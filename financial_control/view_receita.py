from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Receita
from django.contrib.auth.decorators import login_required, permission_required