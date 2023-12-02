from django.db import models
from django import forms
from django.forms import ModelForm
from decimal import Decimal




class bank(models.Model):
    
    
    Account_no = models.CharField(max_length=250)
    Name = models.CharField(max_length=250)
    Balance = models.IntegerField()
    amount = models.DecimalField(max_digits= 10 , decimal_places= 2,default='0' )



class AmountFrom(forms.Form):
    amount = forms.DecimalField(label='Amount',max_digits= 10 , decimal_places= 2 )
    
class Transactions(ModelForm):
    class Meta:
        model = bank
        fields = ['amount']
