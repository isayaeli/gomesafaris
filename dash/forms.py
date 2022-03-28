from django import forms
from django.forms import ModelForm
from dash.models import UserTracker

class TrackForm(ModelForm):
    place_1 =  forms.BooleanField(required=False)
    place_2 =  forms.BooleanField(required=False)
    place_3 =  forms.BooleanField(required=False)
    place_4 =  forms.BooleanField(required=False)
    place_5 =  forms.BooleanField(required=False)
    place_6 =  forms.BooleanField(required=False)
    place_7 =  forms.BooleanField(required=False)

    class Meta:
    	model= UserTracker
    	fields = '__all__'