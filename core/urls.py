from django.db.models.query import create_namedtuple_class
from django.urls import include, path

from core.views import CreateTrade, ListTrades

app_name = "core"
urlpatterns = [
    path("create/", CreateTrade.as_view(), name="createtrade"),
    path("list/", ListTrades.as_view(), name="listtrades"),
]
