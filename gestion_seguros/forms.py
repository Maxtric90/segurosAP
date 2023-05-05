from django import forms

TYPE_CHOICES={
    ("general", "General"),
    ("diploma_tramite", "Diploma en trámite"),
    ("otros", "Otros")
}

class AltaClienteForm(forms.Form):
    razonSocial = forms.CharField(max_length=30, min_length=3, required=True, 
        widget=forms.TextInput(), 
        label="Razón Social (*)")
    CUIT = forms.CharField(max_length=30, min_length=3, required=True, label="CUIT (*)")
    email = forms.EmailField(label="Email (*)", required=True)
    usuario = forms.CharField(max_length=20, min_length=4, required=True, label="Usuario (*)")
    contrasena = forms.CharField(max_length=20, min_length=5, widget=forms.PasswordInput, required=True, label="Cotnraseña (*)")
    domicilio = forms.CharField(max_length=60, required=False, label="Domicilio")
    telefono = forms.IntegerField(required=False, label="Telefono")


class Enviarconsultaforma(forms.Form):
    mail=forms.EmailField(label="Email ", required=True)
    tipo = forms.ChoiceField(
        choices=TYPE_CHOICES,
    )
    fecha = forms.DateField(
        widget=forms.SelectDateWidget()
    )
    mensaje = forms.CharField(widget=forms.Textarea)