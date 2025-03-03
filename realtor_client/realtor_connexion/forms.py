from django import forms

class OdooLoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    password = forms.CharField(
        max_length=100,
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
    )
class OdooSignInForm(forms.Form):
    email = forms.EmailField( max_length=100,
                             label="Email", 
                             widget=forms.TextInput(attrs={'class': 'form-control'}),
                             required=True)
    username = forms.CharField(
        max_length=100,
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    password = forms.CharField(
        max_length=100,
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
    )
    