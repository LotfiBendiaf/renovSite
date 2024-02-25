from django.shortcuts import render
from .forms import MessageForm

# Create your views here.
def Home(request):

    return render(request, 'home.html')

# Travaux
def Travaux(request):

    return render(request, 'travaux.html')
# A Propos
def Apropos(request):

    return render(request, 'apropos.html')
# FAQ
def FAQ(request):

    return render(request, 'FAQ.html')
# Conditions
def Conditions(request):

    return render(request, 'conditions.html')

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
