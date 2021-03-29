from django.urls import path

from .views import ClientCreateView

app_name = 'clients'


urlpatterns = [
    path('new', ClientCreateView.as_view()),
]
