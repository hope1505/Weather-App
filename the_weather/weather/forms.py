from django.forms import ModelForm, TextInput
from .models import City 
from django import forms

class CityForm(ModelForm):
    class Meta:
        model = City 
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}
        

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label="Name")
    contact_email = forms.EmailField(required=True, label="Email")
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="Message"
    )        
        
        