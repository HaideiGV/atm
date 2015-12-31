from django.db import models

class Card(models.Model):
    number = models.IntegerField(unique=True, max_length=14)
    status = models.BooleanField()
    pin = models.IntegerField(unique=True, max_length=4)



class Transactions(models.Model):
    card_number = models.ForeignKey(Card.number)
    date = models.DateTimeField()
    balance = models.BooleanField()
    paymant = models.FloatField()
    transaction_status = models.IntegerField(max_length=10)
