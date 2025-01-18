from django.contrib import admin
from .models import (
    Proyecto, Presupuesto, Fase, Etapa,
    Categoria, Clasificacion, Tienda, Proveedor,
    Contratista, RegistroContratista, Material, Inventario,
    DocumentoProyecto
)

# Configuración de Proyecto
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin', 'estado', 'descripcion_corta')
    search_fields = ('nombre', 'estado')
    list_filter = ('estado', 'fecha_inicio', 'fecha_fin')
    ordering = ('estado', 'fecha_inicio')
    
    def descripcion_corta(self, obj):
        return (obj.descripcion[:50] + '...') if len(obj.descripcion) > 50 else obj.descripcion
    descripcion_corta.short_description = 'Descripción'

# Configuración de Presupuesto
@admin.register(Presupuesto)
class PresupuestoAdmin(admin.ModelAdmin):
    list_display = ('proyecto', 'monto_total', 'monto_gastado', 'monto_restante')
    search_fields = ('proyecto__nombre',)
    list_filter = ('monto_total',)
    
    def monto_restante(self, obj):
        return obj.calcular_monto_restante()
    monto_restante.short_description = 'Monto Restante'

# Configuración de Fase
@admin.register(Fase)
class FaseAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion_corta')
    search_fields = ('nombre',)
    
    def descripcion_corta(self, obj):
        return (obj.descripcion[:50] + '...') if len(obj.descripcion) > 50 else obj.descripcion
    descripcion_corta.short_description = 'Descripción'

# Configuración de Etapa
@admin.register(Etapa)
class EtapaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fase', 'descripcion_corta')
    search_fields = ('nombre', 'fase__nombre')
    
    def descripcion_corta(self, obj):
        return (obj.descripcion[:50] + '...') if len(obj.descripcion) > 50 else obj.descripcion
    descripcion_corta.short_description = 'Descripción'

# Configuración de Categoría
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion_corta')
    search_fields = ('nombre',)
    
    def descripcion_corta(self, obj):
        return (obj.descripcion[:50] + '...') if len(obj.descripcion) > 50 else obj.descripcion
    descripcion_corta.short_description = 'Descripción'

# Configuración de Clasificación
@admin.register(Clasificacion)
class ClasificacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion_corta')
    search_fields = ('nombre',)
    
    def descripcion_corta(self, obj):
        return (obj.descripcion[:50] + '...') if len(obj.descripcion) > 50 else obj.descripcion
    descripcion_corta.short_description = 'Descripción'

# Configuración de Tienda
@admin.register(Tienda)
class TiendaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'descripcion_corta')
    search_fields = ('nombre', 'direccion')
    
    def descripcion_corta(self, obj):
        return (obj.descripcion[:50] + '...') if len(obj.descripcion) > 50 else obj.descripcion
    descripcion_corta.short_description = 'Descripción'

# Configuración de Proveedor
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contacto', 'direccion')
    search_fields = ('nombre', 'contacto')

# Configuración de Contratista
@admin.register(Contratista)
class ContratistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especialidad', 'tipo_contratista', 'descripcion_corta')
    search_fields = ('nombre', 'especialidad', 'tipo_contratista')
    list_filter = ('tipo_contratista',)
    
    def descripcion_corta(self, obj):
        return (obj.descripcion[:50] + '...') if len(obj.descripcion) > 50 else obj.descripcion
    descripcion_corta.short_description = 'Descripción'

# Configuración de RegistroContratista
@admin.register(RegistroContratista)
class RegistroContratistaAdmin(admin.ModelAdmin):
    list_display = ('proyecto', 'etapa', 'contratista', 'descripcion_servicio', 'costo_servicio', 'fecha_servicio')
    search_fields = ('proyecto__nombre', 'etapa__nombre', 'contratista__nombre', 'descripcion_servicio')
    list_filter = ('fecha_servicio', 'proyecto', 'etapa')

# Configuración de Material
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'unidad', 'categoria', 'clasificacion')
    search_fields = ('nombre', 'categoria__nombre', 'clasificacion__nombre')
    list_filter = ('categoria', 'clasificacion')

# Configuración de Inventario
@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('material', 'proyecto', 'etapa', 'cantidad', 'precio_unitario', 'subtotal', 'tienda', 'proveedor', 'facturado', 'fecha')
    search_fields = ('material__nombre', 'proyecto__nombre', 'etapa__nombre')
    list_filter = ('facturado', 'fecha', 'proyecto')

# Configuración de DocumentoProyecto
@admin.register(DocumentoProyecto)
class DocumentoProyectoAdmin(admin.ModelAdmin):
    list_display = ('proyecto', 'documento', 'fecha_subida', 'descripcion_corta')
    search_fields = ('proyecto__nombre',)
    list_filter = ('fecha_subida',)
    
    def descripcion_corta(self, obj):
        return (obj.descripcion[:50] + '...') if len(obj.descripcion) > 50 else obj.descripcion
    descripcion_corta.short_description = 'Descripción'


