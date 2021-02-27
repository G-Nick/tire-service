from django.views.generic import ListView

from .models import Car


class CarsList(ListView):
    template_name = 'cars_list.html'
    model = Car
    context_object_name = 'cars'
