# Importa pytest para definir pruebas automáticas
import pytest
# reverse permite resolver nombres de URLs en rutas reales
from django.urls import reverse
# Importamos el modelo que vamos a usar para poblar datos de prueba
from etiquetas.models import Etiqueta
# Para generar fechas
from datetime import date
# Librerías para leer archivos Excel generados por la vista
import openpyxl
from io import BytesIO
# ======================== TEST: Vista de reportes con filtros ========================
@pytest.mark.django_db  # Usa la base de datos de pruebas
def test_reportes_view_filtrado(client, etiqueta):
    url = reverse("reportes")  # Obtiene la URL de la vista "reportes"
    response = client.get(url, {
        "lote": "12556",         # Aplica filtro por lote
        "area": "Linea 1 Noche",       # Aplica filtro por área
        "turno": "Dia",
        "fecha": "2025-01-24", 
        "mes_proceso": "1", 
        "calidad": "INDUSTRIAL A"
    })
    assert response.status_code == 200         # Verifica que la respuesta fue exitosa
    assert b"12556" in response.content          # Confirma que el lote filtrado aparece en el HTML

# ======================== TEST: Exportación a Excel ========================
@pytest.mark.django_db
def test_export_to_excel(client, etiqueta):
    url = reverse("export_to_excel")  # Obtiene la URL de la vista que exporta Excel
    response = client.get(url, {"lote": "12556", "area": "Linea 1 Noche",       # Aplica filtro por área
        "turno": "Dia",
        "mes_proceso": "1", 
        "calidad": "INDUSTRIAL A"})  # Simula GET con filtro por lote

    assert response.status_code == 200
    assert response["Content-Type"] == "application/vnd.ms-excel"  # Verifica que se devuelve un archivo Excel

    # Convierte los bytes del archivo en un libro de Excel usable
    wb = openpyxl.load_workbook(BytesIO(response.content))
    ws = wb.active  # Obtiene la hoja activa (la primera)

    assert ws.cell(row=1, column=1).value == "DiaProceso"  # Verifica que el primer encabezado sea correcto

# ======================== TEST: Exportación a PDF ========================
@pytest.mark.django_db
def test_export_to_pdf(client, etiqueta):
    url = reverse("export_to_pdf")  # Obtiene la URL de la vista que exporta PDF
    response = client.get(url, {"lote": "12556", "area": "Linea 1 Noche",       # Aplica filtro por área
        "turno": "Dia",
        "mes_proceso": "1", 
        "calidad": "INDUSTRIAL A"})  # Simula GET con filtro por lote

    assert response.status_code == 200
    assert response["Content-Type"] == "application/pdf"  # Verifica que se devuelve un archivo PDF
    
    # ======================== TEST: Estadísticas de producción ========================
@pytest.mark.django_db
def test_estadisticas_view(client, etiqueta):
    # Accede a la vista de estadísticas (requiere al menos una etiqueta cargada)
    response = client.get(reverse("estadisticas"))
    assert response.status_code == 200

    # Verifica que se cargan las variables necesarias para los gráficos
    assert b"destinos" in response.content or b"fechas" in response.content
