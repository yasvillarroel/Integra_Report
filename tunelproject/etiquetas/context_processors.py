from .models import Usuario

def rol_usuario(request):
    if request.user.is_authenticated:
        try:
            usuario = Usuario.objects.get(email_user=request.user.email)
            return {'es_admin_personalizado': usuario.id_rol.id_rol in [11, 21]}
        except Usuario.DoesNotExist:
            return {'es_admin_personalizado': False}
    return {'es_admin_personalizado': False}

