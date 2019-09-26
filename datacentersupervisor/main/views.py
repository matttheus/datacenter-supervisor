from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Temperature, Humidity, Gas


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core.html')


class TemperatureView(ListView):
    model = Temperature
    paginate_by = 10


class HumidityView(ListView):
    model = Humidity
    paginate_by = 10


class GasView(ListView):
    model = Gas
    paginate_by = 10