from django import forms
from .models import Mueble, Categoria, Proveedor, Cliente, Venta

class MuebleForm(forms.ModelForm):
    class Meta:
        model = Mueble
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'proveedor', 'stock']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            'precio': forms.NumberInput(attrs={'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'min': '0'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'email']
        
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'mueble', 'cantidad', 'fecha_venta']
        widgets = {
            'fecha_venta': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.all()
        self.fields['mueble'].queryset = Mueble.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        mueble = cleaned_data.get('mueble')
        cantidad = cleaned_data.get('cantidad')

        if mueble and cantidad and cantidad > mueble.stock:
            self.add_error('cantidad', 'No hay suficiente stock para esta cantidad.')

        return cleaned_data
    
class MuebleFilterForm(forms.Form):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        required=False,
        label='Categoría'
    )
    min_stock = forms.IntegerField(
        required=False,
        label='Mínimo Stock',
        widget=forms.NumberInput(attrs={'placeholder': 'Cantidad mínima'})
    )