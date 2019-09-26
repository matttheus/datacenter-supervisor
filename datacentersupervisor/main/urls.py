from django.urls import path
from .views import TemperatureView, HumidityView, GasView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('index', IndexView.as_view(), name='index'),
    path('temperature/', TemperatureView.as_view(), name='temperature'),
    path('humidity/', HumidityView.as_view(), name='humidity'),
    path('gas/', GasView.as_view(), name='gas'),
]
