from django import forms


class CustomerForm(forms.Form):
    customer_email = forms.EmailField(label='Your email')
