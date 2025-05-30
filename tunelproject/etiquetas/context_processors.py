from .models import Usuario

def rol_usuario(request):
    if request.user.is_authenticated:
        try:
            usuario = Usuario.objects.get(nombre_user=request.user.username)
            return {'es_admin_personalizado': usuario.id_rol.id_rol == 21}
        except Usuario.DoesNotExist:
            return {'es_admin_personalizado': False}
    return {'es_admin_personalizado': False}
