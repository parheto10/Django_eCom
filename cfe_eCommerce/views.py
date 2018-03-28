from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ContactForm, LoginForm, RegisterForm

def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form": login_form,
    }
    print("Utilisateur deja conncter !")
    # print(request.user.is_authenticated())
    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        #print(request.user.is_authenticated())
        if user is not None:
            # print(request.user.is_authenticated())
            login(request, user)
            #context['form'] = LoginForm()
            return redirect("/")
        else:
            print('Error')
    return render(request, 'auth/login.html', context)

User = get_user_model()
def insription(request):
    register_form = RegisterForm(request.POST or None)
    context = {
        'form': register_form,
    }
    if register_form.is_valid():
        print(register_form.cleaned_data)
        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        new_user =  User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, 'auth/register.html', context)

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