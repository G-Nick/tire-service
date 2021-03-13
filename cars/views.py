from django.views.generic import ListView, DetailView

from .models import Car


class CarList(ListView):
    template_name = 'cars_list.html'
    model = Car
    context_object_name = 'cars'


class CarDetailView(DetailView):
    template_name = 'car.html'
    model = Car
    context_object_name = 'car'
