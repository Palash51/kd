# from django import forms

# class RegistrationForm(forms.Form):
# 	first_name = forms.CharField(max_length=45)
# 	last_name = forms.CharField(max_length=45)
# 	email = forms.EmailField()
# 	password = forms.CharField(max_length=100,widget=forms.PasswordInput)
# 	confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput)	


from django.contrib.auth.forms import AuthenticationForm 
from django import forms

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(forms.Form):
    Name = forms.CharField(label="Name", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'Name': 'Name'}))

    Phone = forms.IntegerField(label="Phone",  
                               widget=forms.TextInput(attrs={'class': 'form-control', 'Phone': 'Phone'}))

    FieldLocation = forms.CharField(label="Field Location", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'FieldLocation': 'FieldLocation'}))

    CropAcres = forms.IntegerField(label="Field Area(in acres)", 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'CropAcres': 'CropAcres'}))