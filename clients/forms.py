from django import forms

from .models import Client, ClientCar


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
