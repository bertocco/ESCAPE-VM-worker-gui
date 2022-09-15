
from django.shortcuts import render
from django import forms

class CreatevmForm(forms.Form):

    access_token = forms.CharField(max_length=3000, label='Access Token*')
    machine_name = forms.CharField(max_length=25, label='Provide a server name*')
    ssh_access_key = forms.CharField(max_length=100, label="Pre-loaded ssh key name*")

