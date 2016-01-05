from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse
import datetime
from cash.models import *

def card_number_page(request):
    cards = Card.objects.all()
    card = request.GET['card']
    if card in cards:
        return HttpResponseRedirect('/cash/pin/')
    else:
        return render(request, "card_number_page.html")

def pin_code_page(request):
    btn = request.POST.get('button')
    if btn == 'exit':
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