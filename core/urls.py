from django.db.models.query import create_namedtuple_class
from django.urls import include, path

from core.views import (
    CounterPartyCreateView,
    CreateProduct,
    CreateTrade,
    ListCounterParties,
    ListProducts,
    ListTrades,
    add_counter_party,
)

app_name = "core"
urlpatterns = [
    path("create_trade/", CreateTrade.as_view(), name="createtrade"),
    path(
        "create_counterparty/",
        CounterPartyCreateView.as_view(),
        name="createcounterparty",
    ),
    path("create_product/", CreateProduct.as_view(), name="createproduct"),
    path("list_trade/", ListProducts.as_view(), name="listproducts"),
    path("list_product/", ListTrades.as_view(), name="listtrades"),
    path("list_counterparty/", ListCounterParties.as_view(), name="listcounterparty"),
    path("add-counterparty/", add_counter_party, name="add-counterparty"),
]
