from django.db import models

class Card(models.Model):
    number = models.IntegerField(unique=True)
    status = models.BooleanField()
    pin = models.IntegerField()

    def __repr__(self):
        return str(self.number)



class Transactions(models.Model):
    card_number = models.ForeignKey(Card)
    date = models.DateTimeField()
    balance = models.BooleanField()
    paymant = models.FloatField()
    transaction_status = models.IntegerField()

    def __unicode__(self):
        return str(self.card_number)+str(self.date)+str(self.transaction_status)+str(self.paymant)
