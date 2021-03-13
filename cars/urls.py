from django.urls import path

from .views import CarList, CarDetailView

app_name = 'cars'


urlpatterns = [
    path('', CarList.as_view()),
    path('<int:pk>', CarDetailView.as_view(), name='detail')
]
