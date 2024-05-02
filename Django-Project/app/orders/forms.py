from django import forms


class CreateOrderForm(forms.Form):
    email = forms.EmailField()

