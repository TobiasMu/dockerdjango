from django.db.models.query import create_namedtuple_class
from django.urls import include, path

from core.views import CreateProduct, CreateTrade, ListProducts, ListTrades

app_name = "core"
urlpatterns = [
    path("create_trade/", CreateTrade.as_view(), name="createtrade"),
    path("create_product/", CreateProduct.as_view(), name="createproduct"),
    path("list_trade/", ListProducts.as_view(), name="listproducts"),
    path("list_product/", ListTrades.as_view(), name="listtrades"),
]
