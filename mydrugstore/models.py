from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse


# Create your models here.

class Producte(models.Model):
    Nom = models.TextField()
    Descripcio = models.TextField()
    Photo = models.ImageField(upload_to='photos/')

    def __unicode__(self):
        return u"%s" % self.name

class Estoc(models.Model):
    Producte = models.ForeignKey(Producte, default = 1, on_delete = models.CASCADE)
    Quantitat = models.IntegerField()

    def __unicode__(self):
        return u"%s" % self.name

class Cataleg(models.Model):
    Producte = models.ForeignKey(Estoc, default = 1, on_delete = models.DO_NOTHING)
    Prize = models.FloatField(null = True)

    def __unicode__(self):
        return u"%s" % self.name

class Proveedor(models.Model):
    Nom = models.TextField()
    Descripcio = models.TextField()
    Productes = models.ForeignKey(Producte, default = models.SET_NULL, on_delete = models.DO_NOTHING)

    def __unicode__(self):
        return u"%s" % self.name

class Usuari(models.Model):
    name = models.TextField()
    Password = models.TextField()
    CreditCard = models.IntegerField()

    def __unicode__(self):
        return u"%s" % self.name

class CarritoDeCompra(models.Model):
    ProducteId = models.IntegerField()
    Prize = models.ForeignKey(Cataleg, default = 1, on_delete = models.CASCADE)
    Discount = models.FloatField()
    User = models.ForeignKey(Usuari, default = 1, on_delete = models.SET_DEFAULT)

    def __unicode__(self):
        return u"%s" % self.name


