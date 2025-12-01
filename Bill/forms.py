from django import forms
from .models import Bill

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = '__all__'
        widgets = {
            'receive_date': forms.DateInput(format='%d-%m-%Y', attrs={'type':'date'}),
            'payment_date': forms.DateInput(format='%d-%m-%Y', attrs={'type':'date'}),
        }
