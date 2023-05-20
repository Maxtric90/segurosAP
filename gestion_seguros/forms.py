from django import forms
from django.core.exceptions import ValidationError
from .models import Cliente

TYPE_CHOICES={
    ("general", "General"),
    ("diploma_tramite", "Diploma en trámite"),
    ("otros", "Otros")
}

class AltaClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

    widgets = {
        "contrasena": forms.PasswordInput()
    }

    def clean(self):
        documento = self.cleaned_data["documento"]
        if Cliente.objects.filter(documento = documento).exists():
            raise ValidationError("Ya hay un cliente inscripto con ese documento")
        
        return self.cleaned_data

class Enviarconsultaforma(forms.Form):
    mail=forms.EmailField(label="Email ", required=True)
    tipo = forms.ChoiceField(
        choices=TYPE_CHOICES,
    )
    fecha = forms.DateField(
        widget=forms.SelectDateWidget()
    )
    mensaje = forms.CharField(widget=forms.Textarea)