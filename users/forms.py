from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class loginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'username'}), label='Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}), label='Password')



class RegisterForm(UserCreationForm):
    username = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Username '}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),label= "Email")
    password1 = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),label="Password")
    password2 = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control','width':'30px'}),label="Confirm Password")

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username','email','password1','password2')

    # def save(self, commit=True):
    #     user = super(RegisterForm, self).save(commit=False)
    #     user = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user