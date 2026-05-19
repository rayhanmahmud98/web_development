from django import forms

class TeachersRegistration(forms.Form):
    first_name = forms.CharField(label="Enter Your First Name", label_suffix = ' : ')
    last_name = forms.CharField(label="Enter Your Last Name", label_suffix = ' : ')
    email = forms.EmailField(initial='rayhaniiuc48@gmail.com')
    password = forms.CharField(widget=forms.PasswordInput)
