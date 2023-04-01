from django import forms
from django.forms import DateTimeInput
from .models import Tarea, Producto, Proveedor, Visitas


class TareaForm (forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'cliente', 'descripcion', 'material',
                  'importante', 'usuario', 'proveedor', 'modelo', 'cantidad']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'material': forms.TextInput(attrs={'class': 'form-control'}),
            'importante': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'modelo':  forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),

        }


class VisitasForm(forms.ModelForm):
    class Meta:
        model = Visitas
        fields = "__all__"
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control'}),
            'visita': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'ubicacion': forms.URLInput(attrs={'class': 'form-control'})
        }




class ProveedorForm (forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['proveedor']


class ProductoForm (forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['modelo', 'ficha_tecnica']


class FormularioContacto(forms.Form):

    nombre = forms.CharField(label="Nombre", required=True)

    email = forms.CharField(label="Email", required=True)

    contenido = forms.CharField(label="Contenido", widget=forms.Textarea)
