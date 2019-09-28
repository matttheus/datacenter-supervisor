from django.urls import path
from .views import CollectionView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('index', IndexView.as_view(), name='index'),
    path('collect/', CollectionView.as_view(), name='collect'),
]
