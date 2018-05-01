from django import forms
from django.contrib.auth import get_user_model



class ContactForm(forms.Form):
    nom = forms.CharField(widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nom et Prenoms"
            }
        )
    )
    email = forms.EmailField(widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email"
            }
        )
    )
    contenu = forms.CharField(widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Mon Message"
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Veuillez Entrez une Adresse gmail.com")
        raise email


