from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Card, Profile
from .forms import RegistrationForm, LoginForm
import random
from django.views.generic.edit import DeleteView
from datetime import datetime, timedelta


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            if form.cleaned_data['password'] == form.cleaned_data['rep_password']:
                new_user.set_password(form.cleaned_data['password'])
                new_user.save()
                return render(request, 'registration/registration_done.html', {'form': form})
            else:
                return render(request, 'registration/registration.html', {'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'registration/registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data()
            user = authenticate(request, username=cd['username'], password=cd['password'])
            login(request, user)
    else:
        login_form = LoginForm()
        return render(request, 'register/login.html', {'login_form': login_form})


@login_required
def profile_cards(request):
    cards = Card.objects.filter(profile=request.user)
    paginator = Paginator(cards, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'card/cards.html', {'cards': cards, 'page_obj': page_obj})


@login_required
def new_card(request):
    card = Card.objects.create(profile=request.user,
                               series=random.randint(1000, 9999),
                               number=random.randint(100000000000, 999999999999),
                               ended_at=datetime.now()+timedelta(days=365),
                               status='Active')
    return HttpResponse('Yo, U have a new card, check your cards, for more info')


@login_required
def delete_card(request, id):
    cards = Card.objects.filter(profile=request.user)
    card = Card.objects.get(id=id).delete()
    return render(request, 'card/cards.html', {'card': card, 'cards': cards})


@login_required
def deactivate_card(request, id):
    cards = Card.objects.filter(profile=request.user)
    card = Card.objects.filter(id=id).update(status=Card.status_choices[1][1])
    return render(request, 'card/cards.html', {'card': card, 'cards': cards})


@login_required
def activate_card(request, id):
    cards = Card.objects.filter(profile=request.user)
    card = Card.objects.filter(id=id).update(status=Card.status_choices[0][1])
    return render(request, 'card/cards.html', {'card': card, 'cards': cards})


def profile(request):
    return render(request, 'accounts/profile.html')
