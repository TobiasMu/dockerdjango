from django.db.models.query import create_namedtuple_class
from django.urls import path, include

from core.views import CreateTrade

urlpatterns = [path("create/", CreateTrade.as_view(), name="createtrade")]
