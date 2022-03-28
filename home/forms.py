from django import forms
from .models import  Contact

class contactForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder':'first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder':'last name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control ', 'placeholder':'email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder':'phone'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder':'location'}))
    destination = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder':'location'}))
    flight =  forms.BooleanField(required=False)
    accomodation =  forms.BooleanField(required=False)
    pick_up =  forms.BooleanField(required=False)
    tour_cars =  forms.BooleanField(required=False)

    class Meta:
        model = Contact
        fields = '__all__'