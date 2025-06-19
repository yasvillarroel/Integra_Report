# ======================== IMPORTACIONES ========================
import pytest  # Framework de testing
from django.urls import reverse  # Para resolver nombres de rutas Django
from django.core.files.uploadedfile import SimpleUploadedFile  # Para simular archivos subidos
from etiquetas.models import Usuario, RolUser  # Modelos personalizados
from django.contrib.auth.models import User  # Usuario base de Django
import pandas as pd  # Para generar un archivo Excel en memoria
from io import BytesIO  # Para manejar archivos binarios sin guardarlos físicamente

# ======================== TEST: Cargar archivo Excel ========================
@pytest.mark.django_db
def test_cargar_archivo_excel(client):
    # 1. Crear el rol y los usuarios (Django y personalizado)
    rol = RolUser.objects.create(id_rol=51, nom_rol="digitador")
    
    user_django = User.objects.create_user(
        username="cargador",
        password="12345",
        email="carga@test.com"
    )

    user_personal = Usuario.objects.create(
        nombre_user="cargador",
        apellido_user="Test",
        email_user="carga@test.com",
        pass_user="12345",
        id_rol=rol
    )

    # 2. Loguearse como usuario
    client.login(username="cargador", password="12345")

    # 3. Crear un archivo Excel válido en memoria con pandas
    df = pd.DataFrame([{
        "diaproceso": "2025-06-19",
        "codigobarra": "000001TEST",
        "lote": "TEST123",
        "area": "Área Test",
        "destinoproducto": "Producto Test",
        "totalkilos": 10.0,
        "totalbandejas": 5,
        "horaproceso": "12:00",
        "horaintervalo": "12-13 hrs",
        "turno": "Día",
        "mesproceso": "2025-06",
        "fechaproduccion": "2025-06-19",
        "diaproceso2": "2025-06-19"
    }])

    # Guardar el DataFrame en un archivo binario en memoria
    buffer = BytesIO()
    df.to_excel(buffer, index=False)
    buffer.seek(0)  # Regresa al inicio del buffer para que pueda ser leído

    # 4. Simular un archivo subido con SimpleUploadedFile (como si fuera un archivo real .xlsx)
    file_data = SimpleUploadedFile(
        "test_archivo.xlsx",  # nombre simulado
        buffer.read(),  # contenido del archivo en binario
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    # 5. Simular una petición POST al endpoint que recibe archivos
    response = client.post(reverse("cargar_archivo"), {
        "archivo_excel": file_data  # lo envía como si fuera un input[type="file"]
    }, follow=True)

    # 6. Verificar que la respuesta fue exitosa y contiene el mensaje de éxito esperado
    assert response.status_code == 200
    assert b"Archivo cargado y datos procesados exitosamente" in response.content
