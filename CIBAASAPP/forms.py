from django import forms
from .models import *


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'fecha_inicio', 'fecha_fin', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Proyecto'}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Detalles del Proyecto'}),
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Categoría'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Detalles de la Categoría'}),
        }


class ClasificacionForm(forms.ModelForm):
    class Meta:
        model = Clasificacion
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Clasificación'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Detalles de la Clasificación'}),
        }


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nombre', 'unidad', 'categoria', 'clasificacion', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Material'}),
            'unidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unidad de Medida'}),
            'categoria': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Categoria del Material'}),
            'clasificacion': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Categoria del Material'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del Material'}),
        }


class TiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = ['nombre', 'direccion', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Tienda'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección de la Tienda'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Detalles de la Tienda'}),
        }


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'contacto', 'direccion', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Proveedor'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contacto de la Proveedor'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección de la Proveedor'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Detalles de la Proveedor'}),
        }


class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['proyecto', 'etapa', 'material', 'cantidad', 'fecha', 'precio_unitario', 'descuento', 'iva', 'tienda', 'proveedor', 'facturado', 'descripcion']
        widgets = {
            'proyecto': forms.Select(attrs={'class': 'form-select'}),
            'etapa': forms.Select(attrs={'class': 'form-select'}),
            'material': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Cantidad'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio Unitario'}),
            'descuento': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Descuento (%)'}),
            'iva': forms.Select(attrs={'class': 'form-select'}, choices=[(8, '8%'), (16, '16%')]),
            'tienda': forms.Select(attrs={'class': 'form-select'}),
            'proveedor': forms.Select(attrs={'class': 'form-select'}),
            'facturado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del Material'}),
        }


class FaseForm(forms.ModelForm):
    class Meta:
        model = Fase
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Fase'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Detalles de la Fase'}),
        }


class EtapaForm(forms.ModelForm):
    class Meta:
        model = Etapa
        fields = ['nombre', 'descripcion', 'fase']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Etapa'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Detalles de la Etapa'}),
            'fase': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Fase'}),
        }


class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = ['monto_total', 'monto_gastado', 'descripcion']
        widgets = {
            'monto_total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto Total'}),
            'monto_gastado': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto Gastado'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del Presupuesto'}),
        }

    def clean_monto_gastado(self):
        # Si el campo está vacío, retorna 0
        monto_gastado = self.cleaned_data.get('monto_gastado')
        if monto_gastado is None:
            return 0
        return monto_gastado


class DocumentoProyectoForm(forms.ModelForm):
    class Meta:
        model = DocumentoProyecto
        fields = ['documento', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del documento'}),
        }


class ReporteForm(forms.Form):
    proyecto = forms.ModelChoiceField(
        queryset=Proyecto.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True,  # Requerido
        label='Proyecto'
    )
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True,  # Requerido
        label='Fecha de Inicio'
    )
    fecha_fin = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True,  # Requerido
        label='Fecha de Fin'
    )
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False,  # Opcional
        label='Categoría'
    )
    clasificacion = forms.ModelChoiceField(
        queryset=Clasificacion.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False,  # Opcional
        label='Clasificación'
    )
    tienda = forms.ModelChoiceField(
        queryset=Tienda.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False,  # Opcional
        label='Tienda'
    )
    proveedor = forms.ModelChoiceField(
        queryset=Proveedor.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False,  # Opcional
        label='Proveedor'
    )



