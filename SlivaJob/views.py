from django.http import HttpResponse

from .forms import *
from .models import *

from django.shortcuts import render


def index(request):
    return render(request, 'SlivaJob/index.html')


def orders(request):
    return render(request, 'SlivaJob/orders.html')


def workers(request):
    return render(request, 'SlivaJob/workers.html')


def tests(request):
    return HttpResponse("profile")
    #return render(request, 'SlivaJob/test.html', context)

def registration(request):
    context = {}
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
    else:
        sign_up_form = SignUpForm()
    context['sing_up_form'] = sign_up_form
    return render(request, 'SlivaJob/test.html', context)


def profile(request):
    return render(request, 'SlivaJob/profile.html')


def vacancies(request):
    return render(request, 'SlivaJob/vacancies.html')
