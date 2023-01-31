from django.urls import path
from .views import Home, Travaux, Contact, Apropos, FAQ

urlpatterns = [
    path('', Home, name='home'),
    path('travaux/', Travaux, name='travaux'),
    path('contact/', Contact, name='contact'),
    path('apropos/', Apropos, name='apropos'),
    path('FAQ/', FAQ, name='faq'),

]