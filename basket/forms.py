from django import forms


class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    company_name = forms.CharField(max_length=128, required=False)
    country = forms.CharField(max_length=64)
    address = forms.CharField(max_length=255)
    apartment = forms.CharField(max_length=128, required=False)
    city = forms.CharField(max_length=64)
    state = forms.CharField(max_length=64)
    postcode = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)
    email = forms.EmailField()
    notes = forms.CharField(widget=forms.Textarea, required=False)