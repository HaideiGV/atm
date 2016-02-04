from django.db import models

class Card(models.Model):
    number = models.CharField(unique=True, max_length=16)
    status = models.BooleanField()
    pin = models.CharField(max_length=4, null=False)
    amount = models.IntegerField(verbose_name='Cash amount')

    def __repr__(self):
        return self.number



class Transactions(models.Model):
    """
    100 - successfully withdraw cash
    101 - successfully show balance


    200 - error withdraw cash
    201 - wrong pin
    202 - not enough amount
    """
    card_number = models.CharField(max_length=16)
    input_pin = models.CharField(max_length=4, null=True)
    try_pin = models.IntegerField()
    transaction_time = models.DateTimeField()
    show_balance = models.BooleanField()
    sum_withdrawal = models.FloatField()
    transaction_status = models.BooleanField()
    transaction_code = models.IntegerField()

    def __unicode__(self):
        return str(self.card_number)+str(self.transaction_time)+str(self.transaction_status)+str(self.show_balance)
