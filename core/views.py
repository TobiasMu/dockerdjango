from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView
from .models import Trade


class FrontPage(TemplateView):
    template_name = "core/frontpage.html"


class CreateTrade(CreateView):
    model = Trade
    template_name = "core/createtrade.html"
    success_url = reverse_lazy("frontpage")
    fields = ["product", "counterparty", "price", "quantity"]


class ListTrades(ListView):
    model = Trade
    template_name = "core/listtrades.html"
