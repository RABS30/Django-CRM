from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Records

class signUpForm(UserCreationForm):
    email       = forms.EmailField(required=True,
                                   widget=forms.TextInput(attrs={
                                       'class' : 'form-control', 
                                       'placeholder':'Email Address'
                                       }))
    
    firstName   = forms.CharField(max_length=100, 
                                  required=True, 
                                  widget=forms.TextInput(attrs={
                                      'class' : 'form-control', 
                                      'placeholder':'First Name'
                                      }))
    
    lastName    = forms.CharField(max_length=100, 
                                  required=True, 
                                  widget=forms.TextInput(attrs={
                                      'class' : 'form-control', 
                                      'placeholder':'Last Name'
                                      }))
    
    class Meta:
        model = User
        fields = [
            'username',
            'firstName',
            'lastName',
            'email',
            'password1',
            'password2',
        ]
    def __init__(self, *args, **kwargs):
        super(signUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


class addRecordForm(forms.ModelForm):
    firstName   = forms.CharField(max_length=100,
                                  required=True,
                                    widget=forms.TextInput(attrs={
                                        'class' : 'form-control',
                                        'placeholder':'First Name'
                                    }))
    lastName    = forms.CharField(max_length=100,
                                  required=True,
                                    widget=forms.TextInput(attrs={
                                        'class' : 'form-control',
                                        'placeholder':'Last Name'
                                    }))
    address     = forms.EmailField(required=True,
                                    widget=forms.TextInput(attrs={
                                        'class' : 'form-control',
                                        'placeholder':'Email Address'
                                    }))
    phone       = forms.CharField(max_length=100,
                                    required=True,
                                        widget=forms.TextInput(attrs={
                                            'class' : 'form-control',
                                            'placeholder':'Phone Number'
                                        }))       
    city       = forms.CharField(max_length=100,
                                    required=True,
                                        widget=forms.TextInput(attrs={
                                            'class' : 'form-control',
                                            'placeholder':'city'
                                        }))       
    state       = forms.CharField(max_length=100,
                                    required=True,
                                        widget=forms.TextInput(attrs={
                                            'class' : 'form-control',
                                            'placeholder':'state'
                                        }))    
    zipcode     = forms.CharField(max_length=100,
                                    required=True,
                                        widget=forms.TextInput(attrs={
                                            'class' : 'form-control',
                                            'placeholder':'zipcode'
                                        }))  
    
    class Meta :
        model   = Records
        exclude = ['user',]
        
        
