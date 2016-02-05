from django.shortcuts import render, render_to_response, HttpResponseRedirect
import datetime
from models import *
from forms import CardForm, PinForm



codes = {
    'successfully_withdraw_cash': 100,
    'successfully_show_balance': 101,
    'access_true': 102,
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
        href = '/cash/'
        error = 'Your card is blocked! Please, call the bank!'
        return render(request, 'error.html', {'error':error, 'href': href})
    elif not cards and card != None:
        href = '/cash/'
        error = 'Such card number does not exist!'
        return render(request, 'error.html', {'error':error, 'href': href})
    else:
        return render(request, "card_number_page.html", {'form':form})


def pin_code_page(request):
    form = PinForm(request.GET)
    pin = request.GET.get('pin')
    session_number = request.session['number']
    request.session['pin'] = pin
    if request.POST.get('exit'):
        return HttpResponseRedirect('/cash/')
    elif Card.objects.filter(number=session_number, pin=pin) and pin != None:
        request.session["try_pin"] = 0
        t = Transactions(
            card_number=Card.objects.filter(number=request.session['number']).values('id')[0]['id'],
            input_pin=request.session['pin'],
            try_pin=request.session['try_pin'],
            transaction_time=str(datetime.datetime.now()),
            show_balance=False,
            sum_withdrawal=0,
            transaction_status=True,
            transaction_code=codes['access_true']
        )
        t.save()
        return HttpResponseRedirect('/cash/operations/')
    elif pin != Card.objects.filter(number=session_number).values('pin'):
        if request.session["try_pin"] != 3 and pin != None:
            request.session["try_pin"] += 1
            t = Transactions(
                card_number=Card.objects.filter(number=request.session['number']).values('id')[0]['id'],
                input_pin=request.session['pin'],
                try_pin=request.session['try_pin'],
                transaction_time=str(datetime.datetime.now()),
                show_balance=False,
                sum_withdrawal=0,
                transaction_status=False,
                transaction_code=codes['error_show_balance']
            )
            t.save()
            error = 'Wrong pin. Please try once more!'
            href = '/cash/pin/'
            return render(request, 'error.html', {'error':error, 'href':href})
        elif pin != None:
            c = Card.objects.get(number=session_number)
            c.status = False
            c.save()
            t = Transactions(
                card_number=Card.objects.filter(number=request.session['number']).values('id')[0]['id'],
                input_pin=request.session['pin'],
                try_pin=request.session['try_pin'],
                transaction_time=datetime.datetime.now(),
                show_balance=False,
                sum_withdrawal=0,
                transaction_status=False,
                transaction_code=codes['card_blocked']
            )
            t.save()
            href = '/cash/'
            error = 'Your card is blocked! Please, call the bank!'
            return render(request, 'error.html', {'error':error, 'href': href})
    return render(request, "pin.html", {'form':form})



def operations_page(request):
    if "balance" in request.GET and request.GET["balance"] != None:
        return HttpResponseRedirect('/cash/balance/')
    elif "withdraw_cash" in request.GET and request.GET["withdraw_cash"] != None:
        return HttpResponseRedirect('/cash/withdraw_cash/')
    elif "exit" in request.GET and request.GET["exit"] != None:
        return HttpResponseRedirect('/cash/')
    return render(request, "operations.html")



def balance_page(request):
    now = datetime.datetime.now()
    amount = Card.objects.values('amount').filter(number=request.session['number'])[0]['amount']
    t = Transactions(
        card_number=Card.objects.filter(number=request.session['number']).values('id')[0]['id'],
        input_pin=request.session['pin'],
        try_pin=request.session['try_pin'],
        transaction_time=datetime.datetime.now(),
        show_balance=True,
        sum_withdrawal=0,
        transaction_status=True,
        transaction_code=codes['successfully_show_balance']
    )
    t.save()
    ctx = {
        'card':request.session['number'],
        'now':now,
        'amount':amount
    }
    if "prev" in request.GET and request.GET["prev"] != None:
        return HttpResponseRedirect('/cash/operations/')
    elif "exit" in request.GET and request.GET["exit"] != None:
        return HttpResponseRedirect('/cash/')
    return render_to_response("balance_page.html", ctx)



def withdraw_cash_page(request):
    start_amount = Card.objects.values('amount').filter(number=request.session['number'])[0]['amount']
    amount = request.GET.get('amount')
    if amount != None and amount != '':
        if float(amount) <= float(start_amount):
            c = Card.objects.get(number=request.session['number'])
            c.amount = float(start_amount) - float(amount)
            c.save()
            request.session['trans_time'] = str(datetime.datetime.now())
            request.session['withdraw_cash'] = amount
            t = Transactions(
                card_number=Card.objects.filter(number=request.session['number']).values('id')[0]['id'],
                input_pin=request.session['pin'],
                try_pin=request.session['try_pin'],
                transaction_time=str(request.session['trans_time']),
                show_balance=False,
                sum_withdrawal=float(request.session['withdraw_cash']),
                transaction_status=True,
                transaction_code=codes['successfully_withdraw_cash']
            )
            t.save()
            return HttpResponseRedirect('/cash/report/')
        else:
            t = Transactions(
                card_number=Card.objects.filter(number=request.session['number']).values('id')[0]['id'],
                input_pin=request.session['pin'],
                try_pin=request.session['try_pin'],
                transaction_time=str(request.session['trans_time']),
                show_balance=False,
                sum_withdrawal=request.session['withdraw_cash'],
                transaction_status=False,
                transaction_code=codes['no_money']
            )
            t.save()
            href = '/cash/withdraw_cash/'
            error = 'Not enough money on your account!Please, try another amount!'
            return render(request, 'error.html', {'error':error, 'href': href})
    else:
        return render(request, "withdraw_cash.html")


def report_page(request):
    ctx = {
        'card': request.session['number'],
        'trans_time': request.session['trans_time'],
        'withdraw_cash': request.session['withdraw_cash'],
        'amount': Card.objects.values('amount').filter(number=request.session['number'])[0]['amount']
    }
    if "prev" in request.GET and request.GET["prev"] != None:
        return HttpResponseRedirect('/cash/operations/')
    elif "exit" in request.GET and request.GET["exit"] != None:
        return HttpResponseRedirect('/cash/')
    return render_to_response("report.html", ctx)



def error_page(request):
    btn = request.GET.get("prev")
    if btn == 'prev':
        return HttpResponseRedirect('/cash/operations/')
    return render(request, "error.html")


def about(request):
    return render(request, "about.html")


def contacts(request):
    return render(request, "contacts.html")