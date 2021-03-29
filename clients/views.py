from django.views.generic import CreateView

from .forms import ClientForm


class ClientCreateView(CreateView):
    template_name = 'client.html'
    form_class = ClientForm
