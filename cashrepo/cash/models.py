from django.db import models

class Card(models.Model):
    number = models.IntegerField(unique=True)
    status = models.BooleanField()
    pin = models.IntegerField(unique=True)



class Transactions(models.Model):
    card_number = models.ForeignKey(Card)
    date = models.DateTimeField()
    balance = models.BooleanField()
    paymant = models.FloatField()
    transaction_status = models.IntegerField()
