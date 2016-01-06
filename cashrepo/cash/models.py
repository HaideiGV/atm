from django.db import models

class Card(models.Model):
    number = models.CharField(unique=True, max_length=16)
    status = models.BooleanField()
    pin = models.CharField(max_length=4)

    def __repr__(self):
        return self.number



class Transactions(models.Model):
    card_number = models.ForeignKey(Card)
    date = models.DateTimeField()
    balance = models.BooleanField()
    paymant = models.FloatField()
    transaction_status = models.IntegerField()

    def __unicode__(self):
        return str(self.card_number)+str(self.date)+str(self.transaction_status)+str(self.paymant)
