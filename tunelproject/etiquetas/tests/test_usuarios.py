# ======================== IMPORTACIONES ========================
import pytest  # Framework de testing
from django.urls import reverse  # Para resolver nombres de vistas en URLs
from django.contrib.auth.models import User  # Modelo de usuario estándar de Django
from etiquetas.models import Usuario, RolUser  # Modelos personalizados del sistema

# ======================== FIXTURE: Usuario completo con Rol ========================
@pytest.fixture
def usuario_completo(db):
    # Crea un rol de tipo 'admin'
    rol = RolUser.objects.create(id_rol=21, nom_rol="admin")

    # Crea un usuario en la tabla auth_user (Django)
    user_django = User.objects.create_user(
        username="adminuser",
        password="adminpass",
        email="admin@test.com"
    )

    # Crea el perfil en la tabla personalizada 'usuarios'
    user_personal = Usuario.objects.create(
        nombre_user="adminuser",
        apellido_user="Tester",
        email_user="admin@test.com",
        pass_user="adminpass",
        id_rol=rol
    )

    # Devuelve ambos para usarlos en los tests
    return user_django, user_personal

# ======================== TEST: Actualizar perfil ========================
@pytest.mark.django_db
def test_perfil_view_update(client, usuario_completo):
    user, _ = usuario_completo
    client.login(username="adminuser", password="adminpass")  # Login como admin

    # Simula envío de formulario para editar el perfil
    response = client.post(reverse("perfil"), {
        "nombre": "NuevoNombre",
        "apellido": "NuevoApellido",
        "email": "admin@test.com"
    }, follow=True)

    # Verifica que redirige correctamente y aparece mensaje de éxito
    assert response.status_code == 200
    assert b"Perfil actualizado correctamente" in response.content

# ======================== TEST: Ver vista de usuarios ========================
@pytest.mark.django_db
def test_usuarios_view_load(client, usuario_completo):
    user, _ = usuario_completo
    client.login(username="adminuser", password="adminpass")

    # Accede a la vista de usuarios
    response = client.get(reverse("usuarios"))
    assert response.status_code == 200
    assert b"Usuarios" in response.content or b"Perfil" in response.content  # Verifica que se cargue correctamente

# ======================== TEST: Agregar y eliminar usuario ========================
@pytest.mark.django_db
def test_agregar_eliminar_usuario(client, usuario_completo):
    user, _ = usuario_completo
    client.login(username="adminuser", password="adminpass")

    # Simula creación de nuevo usuario por POST
    response = client.post(reverse("agregar_usuario"), {
        "username": "nuevo",
        "apellido": "usuario",
        "email": "nuevo@test.com",
        "password": "test1234",
        "user_type": 21  # Rol admin
    }, follow=True)

    assert response.status_code == 200
    assert "Usuario agregado con éxito" in response.content.decode("utf-8")

    # Busca el usuario recién creado en auth_user
    nuevo_usuario = User.objects.get(username="nuevo")

    # Simula eliminación del usuario
    response = client.get(reverse("eliminar_usuario", args=[nuevo_usuario.id]), follow=True)
    assert response.status_code == 200
    assert "Usuario eliminado correctamente" in response.content.decode("utf-8")

