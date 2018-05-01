from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ContactForm



def home(request):
    context = {
        "titre":"Ceci est ma Page D'accueil !",
        "content": "Bienvenus sur Notre Page d'Accueil",
    }
    if request.user.is_authenticated():
        context["contenu_premium"] = "Bravo, vous etes passer Premium !"
    return render(request, 'home.html', context)

def about(request):
    context = {
        'titre': "Page A Propos",
         "content": "Bienvenus sur Notre Page A Propos"
    }
    return render(request, 'home.html', context)

def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'titre': "Page de Contacts",
        "form" : contact_form,
        "content": "Bienvenus sur Notre Page Contacts"
    }
    if contact_form.is_valid():
        print (contact_form.cleaned_data)
    # if request.method == "POST":
    #     #print(request.POST)
    #     print(request.POST.get('nom'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('contenu'))
    return render(request, 'contacts/vue.html', context)