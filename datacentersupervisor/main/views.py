from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Collection


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core.html')


class CollectionView(ListView):
    # model = Collection
    paginate_by = 17

    def get_queryset(self):
        queryset = Collection.objects.all().order_by('-date')

        return queryset