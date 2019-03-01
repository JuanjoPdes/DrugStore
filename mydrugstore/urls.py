from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from mydrugstore.models import Usuari, Producte, Proveedor, Cataleg, CarritoDeCompra, Estoc
from mydrugstore.form import UsuariForm, ProducteForm, ProveedorForm, CatalegForm, CarritoDeCompraForm, EstocForm
from mydrugstore.views import UsuariCreate, ProducteCreate, ProveedorCreate, CatalegCreate, CarritoDeCompraCreate, \
                              EstocCreate

urlpatterns = [
    url(r'^$',
        ListView.as_view(
            queryset= Producte.objects.filter(date_lte = timezone.now()).order by('-date')[:5],
            context_object_name='latest_restaurant_list',
        ))
]