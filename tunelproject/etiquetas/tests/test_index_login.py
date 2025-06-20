# ========================
# Archivo de pruebas: test_views.py
# ========================

# Importa pytest para marcar pruebas y usar fixtures
import pytest

# reverse permite resolver nombres de vistas en sus URLs reales
from django.urls import reverse


# ======================== TEST: Vista principal ========================

@pytest.mark.django_db
def test_index_view(client, usuario_completo, etiqueta):
    # usuario_completo es un fixture que devuelve (user_django, user_personal)
    user, _ = usuario_completo

    # Autenticación del usuario
    client.login(username="adminuser", password="adminpass")

    # Petición a la vista index
    response = client.get(reverse("index"))
    content = response.content.decode("utf-8")

    # Validaciones
    assert response.status_code == 200
    assert "Sistema de Reportabilidad de Túnel Continuo" in content
    assert "Producción Hoy" in content
    assert "Producción de la Semana" in content
    assert "Calendario" in content
    assert "Producción Mensual" in content

# ======================== TEST: Login exitoso ========================
@pytest.mark.django_db
def test_login_view_success(client, user):
    # Simula un POST con credenciales válidas a la vista de login
    response = client.post(reverse("login"), {
        "username": "testuser",
        "password": "12345"
    })

    # Verifica que redirige al index (status 302 = redirección)
    assert response.status_code == 302


# ======================== TEST: Login fallido ========================
@pytest.mark.django_db
def test_login_view_failure(client):
    # Simula un POST con credenciales incorrectas a la vista de login
    response = client.post(reverse("login"), {
        "username": "wronguser",
        "password": "wrongpass"
    })

    # La respuesta debe seguir siendo 200 (se vuelve a mostrar el formulario)
    assert response.status_code == 200

    # Y debe contener el mensaje de error definido en login.html
    assert b"incorrectos" in response.content
