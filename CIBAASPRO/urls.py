from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from CIBAASAPP import views
from CIBAASAPP.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('inicio/', HomeView.as_view(), name='inicio'),
    path('crear_proyecto/', ProyectoCreateView.as_view(), name='crear_proyecto'),
    path('proyectos/', ProyectoListaView.as_view(), name='proyecto_lista'),
    path('proyectos/cambiar-estado/<int:pk>/', CambiarEstadoProyectoView.as_view(), name='cambiar_estado_proyecto'),
    path('proyecto/<int:pk>/', views.proyecto_detalle, name='proyecto_detalle'),
    path('crear_categoria/', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('categorias/', CategoriaListaView.as_view(), name='categoria_lista'),
    path('categorias/<int:pk>/', CategoriaUpdateView.as_view(), name='categoria_editar'),
    path('crear_clasificacion/', ClasificacionCreateView.as_view(), name='crear_clasificacion'),
    path('clasificacion/', ClasificacionListaView.as_view(), name='clasificacion_lista'),
    path('clasificacion/<int:pk>/', ClasificacionUpdateView.as_view(), name='clasificacion_editar'),
    path('materiales/', views.materiales, name='material_lista'),
    path('materiales/<int:pk>/', MaterialUpdateView.as_view(), name='material_editar'),
    path('crear_material/', MaterialCreateView.as_view(), name='crear_material'),
    path('tiendas/', TiendaListaView.as_view(), name='tienda_lista'),
    path('tiendas/<int:pk>/', TiendaUpdateView.as_view(), name='tienda_editar'),
    path('crear_tienda/', TiendaCreateView.as_view(), name='crear_tienda'),
    path('proveedores/', ProveedorListaView.as_view(), name='proveedor_lista'),
    path('proveedores/<int:pk>/', ProveedorUpdateView.as_view(), name='proveedor_editar'),
    path('crear_proveedores/', ProveedorCreateView.as_view(), name='crear_proveedor'),
    path('fases/', FaseListaView.as_view(), name='fase_lista'),
    path('fases/<int:pk>/', FaseUpdateView.as_view(), name='fase_editar'),
    path('crear_fases/', FaseCreateView.as_view(), name='crear_fase'),
    path('etapas/', EtapaListaView.as_view(), name='etapa_lista'),
    path('etapas/<int:pk>/', EtapaUpdateView.as_view(), name='etapa_editar'),
    path('crear_etapas/', EtapaCreateView.as_view(), name='crear_etapa'),
    path('inventario/', InventarioListaView.as_view(), name='inventario_lista'),
    path('crear_inventario/', InventarioCreateView.as_view(), name='crear_inventario'),
    path('inventario/<int:pk>/', InventarioUpdateView.as_view(), name='inventario_editar'),
    path('proyecto/<int:pk>/', ProyectoDetalleView.as_view(), name='proyecto_detalle'),
    path('proyecto/<int:pk>/presupuesto/crear/', PresupuestoCreateView.as_view(), name='crear_presupuesto'),
    path('proyecto/<int:pk>/presupuesto/editar/', PresupuestoUpdateView.as_view(), name='presupuesto_editar'),
    path('proyecto/<int:pk>/subir_documento/', DocumentoProyectoCreateView.as_view(), name='subir_documento'),
    path('todos_documentos/', TodosDocumentosListView.as_view(), name='todos_documentos'),
    path('reporte/', views.generar_reporte, name='generar_reporte'),
    path('miembros/', include('miembros.urls')),
    path('miembros/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
