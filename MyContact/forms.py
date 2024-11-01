from django import forms 
class contactform2(forms.Form) : 
    firstname   = forms.CharField(max_length=10) 
    lastname    = forms.CharField(max_length=10)
    email = forms.EmailField()
    msg = forms.CharField(widget=forms.Textarea)
