from django.shortcuts import render

# Create your views here.
def Home(request):

    context = {
    }

    return render(request, 'home.html', context)

# Travaux
def Travaux(request):

    context = {
    }

    return render(request, 'travaux.html', context)