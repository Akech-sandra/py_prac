from django import forms
from .models import Details

class DetailsForm(forms.Form):
    full_name = forms.CharField(required = True, widget=forms.widgets.TextInput (attrs={"placeholder":"Name", "class":"form-control" }), label="")
    email = forms.CharField(required = True, widget=forms.widgets.TextInput (attrs={"placeholder":"Email", "class":"form-control" }), label="")
    city = forms.CharField(required = True, widget=forms.widgets.TextInput (attrs={"placeholder":"City", "class":"form-control" }), label="")
    phone_number =  forms.CharField(required = True, widget=forms.widgets.TextInput (attrs={"placeholder":"phone number", "class":"form-control" }), label="")
    
    class DetailsForm(forms.ModelForm):
     class Meta:
        model = Details
        fields = ['full_name', 'email', 'city', 'phone_number'] 

