from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# importing loading from django template
from django.template import loader


# our view which is a function named index

"""class ProductDetail(DetailView):
    model = Producte
    template_name ='templates/product.html'

    def get_context_data(self,**kwargs):
        context = super(RestaurantDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context
    """


def index(request):
    # getting our template
    template = loader.get_template('index.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render())

def oferts(request):
    # getting our template
    template = loader.get_template('oferts.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render())


def home(request):
    # getting our template
    template = loader.get_template('home.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render())


def catalogue(request):
    # getting our template
    template = loader.get_template('catalogue.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render())


def product(request):
    # getting our template
    template = loader.get_template('product.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render())