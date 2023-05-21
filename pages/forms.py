from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class patient_form(UserCreationForm):

    first_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    class Meta:
        model=User
        fields=('username','first_name','last_name','password1','password2','email')

    def __init__(self, *args, **kwargs):
        super(patient_form,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='username'
        self.fields['username'].label='username'
        self.fields['username'].help_text =''

        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Password'
        self.fields['password1'].label='Password'
        self.fields['password1'].help_text =''

        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Confirm Password'
        self.fields['password2'].label='Password Confirmation'
        self.fields['password2'].help_text =''



