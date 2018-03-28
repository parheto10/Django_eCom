from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nom Utilisateur"
            }
        )
    )
    password = forms.CharField(widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Mot de Passe"
            }
        )
    )


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nom Utilisateur"
            }
        )
    )
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Nom et Prenoms"
        }
    )
    )
    password = forms.CharField(widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Mot de Passe"
            }
        )
    )
    password2 = forms.CharField(label="Confirmer Mot de passe", widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Entrez mot de Passe a Nouveau"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Un Utilisateur avec ce Pseudo Existe deja !!")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Un Utilisateur avec cet Adresse Email Existe deja !!")
        return email


    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError('les deux mot de passe ne concorde pas, Verifier !!')
        return data

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


