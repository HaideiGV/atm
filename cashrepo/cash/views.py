from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse, redirect
import datetime
from models import *
from forms import CardForm
import unicodedata

def card_number_page(request):
    form = CardForm(request.GET)
    card = request.GET.get("number")
    cards = Card.objects.filter(number=card, status=1)
    if cards:

        return HttpResponseRedirect('/cash/pin/')
    else:
        return render(request, "card_number_page.html", {'form':form})



def pin_code_page(request):
    btn = request.POST.get('pin')
    if request.POST.get('exit'):
        return HttpResponseRedirect('/cash/')

    return render(request, "pin.html")

def operations_page(request):
    return render(request, "operations.html")

def balance_page(request):
    now = datetime.datetime.now()
    ctx = {
        'card':'1111-1111-1111-1111',
        'now':now,
        'amount':'1000$'
    }
    return render_to_response("balance_page.html", ctx)

def take_cash_page(request):
    return render(request, "take_cash.html")


def report_page(request):
    trans_time = datetime.datetime.now()
    ctx = {
        'card': 'card number',
        'trans_time':trans_time,
        'take_amount':"100$",
        'amount':'900$'
    }
    return render_to_response("report.html", ctx)

def error_page(request):
    btn = request.POST.get('button')
    if btn == 'prev':
        return HttpResponseRedirect('/cash/operations/')
    return render(request, "error.html")