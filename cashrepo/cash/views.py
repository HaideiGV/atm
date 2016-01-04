from django.shortcuts import render


def card_number_page(request):
    return render(request, "card_number_page.html")

def pin_code_page(request):
    return render(request, "pin.html")