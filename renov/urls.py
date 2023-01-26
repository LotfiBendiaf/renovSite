from django.urls import path
from .views import Home, Travaux, Contact

urlpatterns = [
    path('', Home, name='home'),
    path('travaux/', Travaux, name='travaux'),
    path('contact/', Contact, name='contact'),

]