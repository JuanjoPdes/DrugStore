from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from . import views

"""from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from mydrugstore.models import Usuari, Producte, Proveedor, Cataleg, CarritoDeCompra, Estoc
from mydrugstore.form import UsuariForm, ProducteForm, ProveedorForm, CatalegForm, CarritoDeCompraForm, EstocForm
from mydrugstore.views import UsuariCreate, ProducteCreate, ProveedorCreate, CatalegCreate, CarritoDeCompraCreate, \
                              EstocCreat"""

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
]

