from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView
from .models import Product, Trade


class FrontPage(TemplateView):
    template_name = "core/frontpage.html"


class CreateTrade(CreateView):
    model = Trade
    template_name = "core/createtrade.html"
    success_url = reverse_lazy("frontpage")
    fields = ["counterparty", "product", "price", "quantity"]


class CreateProduct(CreateView):
    model = Product
    template_name = "core/createproduct.html"
    success_url = reverse_lazy("frontpage")
    fields = ["product_type", "product_class", "description"]


class ListTrades(ListView):
    model = Trade
    template_name = "core/listtrades.html"


class ListProducts(ListView):
    model = Product
    template_name = "core/listproducts.html"
