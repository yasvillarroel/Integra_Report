import pytest
from django.contrib.auth.models import User
from etiquetas.models import Etiqueta
from datetime import date

@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='12345')

@pytest.fixture
def etiqueta(db):
    return Etiqueta.objects.create(
        DiaProceso=date.today(),
        CodigoBarra="000001",
        Lote="L01",
        Area="Área 1",
        DestinoProducto="Producto X",
        TotalKilos=50.0,
        TotalBandejas=5,
        Corte="Corte 1",
        Calidad="Alta",
        Conservacion="Frío",
        HoraProceso="12:00",
        HoraIntervalo="12-13 hrs",
        Turno="Día",
        MesProceso="2025-06",
        FechaProduccion=date.today(),
        DiaProceso2=date.today()
    )
