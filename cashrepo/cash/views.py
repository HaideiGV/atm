from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse, redirect
import datetime
from models import *
from forms import CardForm, PinForm

codes = {
    """
    Successfully Codes
    """
    'successfully_withdraw_cash': 100,
    'successfully_show_balance': 101,
    'access_true': 102,


    """
    Codes of Errors
    """
    'error_withdraw': 200,
    'error_show_balance': 201,
    'no_money': 202,
    'card_blocked': 203
}


def card_number_page(request):
    form = CardForm(request.GET)
    card = request.GET.get("number")
    request.session["number"] = card
    request.session["try_pin"] = 0
    cards = Card.objects.filter(number=card, status=1)
    card_blocked = Card.objects.filter(number=card, status=0)
    if cards:
        return HttpResponseRedirect('/cash/pin/')
    elif card_blocked:
        error = 'Your card is blocked! Please, call the bank!'
        return render(request, 'error.html', {'error':error})
    else:
        return render(request, "card_number_page.html", {'form':form})


def pin_code_page(request):
    form = PinForm(request.GET)
    pin = request.GET.get('pin')
    session_number = request.session['number']
    if request.POST.get('exit'):
        return HttpResponseRedirect('/cash/')
    elif Card.objects.filter(number=session_number, pin=pin) and pin != None:
        request.session["try_pin"] = 0
        t = Transactions(
            card_number=Card.objects.filter(number=request.session['number']).values('id')[0]['id'],
            input_pin=request.GET.get('pin'),
            try_pin=request.session['try_pin'],
            transaction_time=datetime.datetime.now(),
            show_balance=False,
            sum_withdrawal=0,
            transaction_status=True,
            transaction_code=codes['access_true']
        )
        t.save()
        return HttpResponseRedirect('/cash/operations/')
    elif pin != Card.objects.filter(number=session_number).values('pin'):
        if request.session["try_pin"] != 4 and pin != None:
            request.session["try_pin"] += 1
            t = Transactions(
                card_number=Card.objects.filter(number=request.session['number']).values('id')[0]['id'],
                input_pin=pin,
                try_pin=request.session['try_pin'],
                transaction_time=datetime.datetime.now(),
                show_balance=False,
                sum_withdrawal=0,
                transaction_status=False,
                transaction_code=codes['error_show_balance']
            )
            t.save()
        elif pin != None:
            c = Card.objects.get(number=session_number)
            c.status = False
            c.save()
            t = Transactions(
                card_number=Card.objects.filter(number=request.session['number']).values('id')[0]['id'],
                input_pin=pin,
                try_pin=request.session['try_pin'],
                transaction_time=datetime.datetime.now(),
                show_balance=False,
                sum_withdrawal=0,
                transaction_status=False,
                transaction_code=codes['card_blocked']
            )
            t.save()
            error = 'Your card is blocked! Please, call the bank!'
            return render(request, 'error.html', {'error':error})
    return render(request, "pin.html", {'form':form})



def operations_page(request):
    if request.GET.get('exit'):
        return HttpResponseRedirect('/cash/')
    elif request.GET.get('take_cash'):
        return HttpResponseRedirect('/cash/take_cash/')
    elif request.GET.get('balance'):
        t = Transactions(
            card_number=Card.objects.filter(number=request.session['number']).values('id')[0]['id'],
            input_pin=request.GET.get('pin'),
            try_pin=request.session['try_pin'],
            transaction_time=datetime.datetime.now(),
            show_balance=True,
            sum_withdrawal=0,
            transaction_status=True,
            transaction_code=codes['successfully_show_balance']
        )
        t.save()
        return HttpResponseRedirect('/cash/balance/')
    else:
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



def withdraw_cash_page(request):
    start_amount = Card.objects.values('amount').filter(number=request.session['number'])[0]['amount']
    amount = request.GET.get('amount')
    print(amount)
    if amount != None:
        if float(amount) <= float(start_amount):
            c = Card.objects.get(number=request.session['number'])
            c.amount = float(start_amount) - float(amount)
            c.save()
            val = Card.objects.values('amount').filter(number=request.session['number'])[0]['amount']

            # ctx = {
            #     'card': request.session['number'],
            #     'trans_time': datetime.datetime.now(),
            #     'withdraw_cash': amount,
            #     'amount': val
            # }

            return HttpResponseRedirect('/cash/report/')
        else:
            error = 'Not enough money on your account!'
            return render(request, 'error.html', {'error':error})
    else:
        return render(request, "withdraw_cash.html")


def report_page(request):
    trans_time = datetime.datetime.now()
    ctx = {
        'card': 'card number',
        'trans_time':trans_time,
        'withdraw_cash':"100$",
        'amount':'900$'
    }
    return render_to_response("report.html", ctx)



def error_page(request):
    btn = request.GET.get("prev")
    print(btn)
    if btn:
        return HttpResponseRedirect('/cash/operations/')
    return render(request, "error.html")