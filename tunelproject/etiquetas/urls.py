from django.urls import path # Importa la función path
from .views import agregar_usuario, cargar_archivo_view, editar_usuario, eliminar_usuario, etiquetas, graficos_view, index, login_view, logout_view, export_to_excel, export_to_pdf, estadisticas_view, reportes_view, perfil_view, contraseña_view, usuarios_view # Importa las vistas de la aplicación
from django.contrib.auth import views as auth_views # Para cambiar contraseña

urlpatterns = [
    path('etiquetas/', etiquetas),
    path("", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path('index/', index, name='index'), # Página principal
    
    # Exportaciones
    path("export/excel/", export_to_excel, name="export_to_excel"),
    path("export/pdf/", export_to_pdf, name="export_to_pdf"),
    
    # Secciones principales
    path("estadisticas/", estadisticas_view, name="estadisticas"),
    path("reportes/", reportes_view, name="reportes"),
    
    # Gestión de usuarios
    path('usuarios/', usuarios_view, name='usuarios'),
    path("perfil/", perfil_view, name="perfil"),
    path("cambiar-contraseña/", contraseña_view, name="cambiar-contraseña"),
    
    path("usuarios/agregar/", agregar_usuario, name="agregar_usuario"),
    
    path('usuarios/eliminar/<int:usuario_id>/', eliminar_usuario, name='eliminar_usuario'),
    path('usuarios/editar/<int:usuario_id>/', editar_usuario, name='editar_usuario'),    
    
    
    # Pruebas gráficos
    path('graficos/', graficos_view, name='graficos'),

    path('cargar-archivo/', cargar_archivo_view, name='cargar_archivo'),
]
