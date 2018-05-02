# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from .models import InviteEmail

from .forms import LoginForm, RegisterForm, InviteForm

def invite_vue(request):
    invite_form = InviteForm(request.POST or None)
    context = {
        "form": invite_form,
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if invite_form.is_valid():
        email = invite_form.cleaned_data.get('email')
        new_invite_email = InviteEmail.objects.create(email=email)
        request.session['new_invite_id'] = new_invite_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("comptes:inscription")

    return redirect("comptes:inscription")

def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form": login_form,
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            try:
                del request.session['new_invite_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:

                return redirect("/")
        else:
            print('Error')
    return render(request, 'comptes/login.html', context)

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
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, 'comptes/register.html', context)


# Create your views here.
