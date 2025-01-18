from django.db import models
from django.utils import timezone
from decimal import Decimal


class Proyecto(models.Model):
    ESTADO_CHOICES = [
        ('en_proceso', 'En proceso'),
        ('terminado', 'Terminado'),
    ]

    nombre = models.CharField(max_length=255)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='en_proceso')

    def __str__(self):
        return self.nombre


class Presupuesto(models.Model):
    proyecto = models.OneToOneField(Proyecto, on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=15, decimal_places=2)
    monto_gastado = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    descripcion = models.TextField(blank=True)

    def calcular_monto_restante(self):
        return self.monto_total - self.monto_gastado

    def __str__(self):
        return f"Presupuesto para {self.proyecto.nombre}"


class Fase(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Etapa(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Clasificacion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Tienda(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField(blank=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255, blank=True)
    direccion = models.TextField(blank=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Contratista(models.Model):
    nombre = models.CharField(max_length=255)
    tipo_contratista = models.CharField(max_length=100, choices=[('persona', 'Persona'), ('empresa', 'Empresa')])
    especialidad = models.CharField(max_length=255)  # Ej. Electricista, Plomero, Albañil, etc.
    contacto = models.CharField(max_length=255, blank=True)
    direccion = models.TextField(blank=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"


class RegistroContratista(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    contratista = models.ForeignKey(Contratista, on_delete=models.CASCADE)
    descripcion_servicio = models.CharField(max_length=255)
    costo_servicio = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_servicio = models.DateField()
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.contratista.nombre} - {self.proyecto.nombre} - {self.etapa.nombre} - Servicio: {self.descripcion_servicio}"


class Material(models.Model):
    nombre = models.CharField(max_length=255)
    unidad = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Inventario(models.Model):
    # Otros campos
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, null=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # En porcentaje
    iva = models.PositiveIntegerField(choices=[(8, '8%'), (16, '16%')])
    facturado = models.BooleanField(default=False)
    descripcion = models.TextField(blank=True)

    def calcular_subtotal(self):
        subtotal = self.precio_unitario * self.cantidad
        if self.descuento:
            subtotal -= subtotal * (self.descuento / Decimal('100'))
        subtotal += subtotal * (Decimal(self.iva) / Decimal('100'))
        return subtotal

    def save(self, *args, **kwargs):
        self.subtotal = self.calcular_subtotal()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.material.nombre} usado en {self.proyecto.nombre}"


class DocumentoProyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    documento = models.FileField(upload_to='documentos_proyecto/')
    descripcion = models.TextField(blank=True)
    fecha_subida = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.documento.name} - {self.proyecto.nombre}"
