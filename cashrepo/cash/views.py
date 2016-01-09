from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse, redirect
import datetime
from models import *
from forms import CardForm, PinForm


def card_number_page(request):
    form = CardForm(request.GET)
    card = request.GET.get("number")
    request.session["number"] = card
    request.session["try_pin"] = 0
    cards = Card.objects.filter(number=card, status=1)
    if cards:
        return HttpResponseRedirect('/cash/pin/')
    else:
        return render(request, "card_number_page.html", {'form':form})


def pin_code_page(request):
    form = PinForm(None)
    pin = request.GET.get('pin')
    session_number = request.session['number']
    if request.POST.get('exit'):
        return HttpResponseRedirect('/cash/')
    elif Card.objects.filter(number=session_number, pin=pin):
        request.session["try_pin"] = 0
        return HttpResponseRedirect('/cash/operations/')
    # elif pin != Card.objects.filter(number=session_number, status=1).values('pin')[0]['pin']:
    #     request.session["try_pin"] += 1
    #     print(request.session["try_pin"])
    #     return HttpResponseRedirect('/cash/pin/')
    return render(request, "pin.html", {'form':form})



def operations_page(request):
    btn = request.GET.get('button')
    if request.POST.get('exit'):
        return HttpResponseRedirect('/cash/', {'url':'/cash/'})
    elif btn == 'take_cash':
        return HttpResponseRedirect('/cash/take_cash/', {'url':'/cash/take_cash/'})
    elif btn == 'balance':
        return HttpResponseRedirect('/cash/balance/')
    return render(request, "operations.html")



def balance_page(request):
    now = datetime.datetime.now()
    amount = Card.objects.values('amount').filter(number=request.session['number'])[0]['amount']
    ctx = {
        'card':request.session['number'],
        'now':now,
        'amount':amount
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
    btn = request.GET.get("prev")
    print(btn)
    if btn:
        return HttpResponseRedirect('/cash/operations/')
    return render(request, "error.html")