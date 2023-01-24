from django.urls import path
from .views import Home, Travaux

urlpatterns = [
    path('', Home, name='home'),
    path('travaux/', Travaux, name='travaux'),

]