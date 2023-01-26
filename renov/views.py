from django.shortcuts import render
from .forms import MessageForm

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

def Contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            print('Saved')
            form.save()
            form = MessageForm()
        else:
            print('Errors: ', form.errors)
    else:
        form = MessageForm()

    context = {
        'form': form,
    }
    
    return render(request, 'contact.html', context)
