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
        CodigoBarra="20251255603000151",
        Lote="12556",
        Area="Linea 1 Noche",
        DestinoProducto="X EMPACAR P/MEMBERS",
        TotalKilos=476.96,
        TotalBandejas=24,
        Corte="PORCION S/PIEL",
        Calidad="INDUSTRIAL A",
        Conservacion="CONGELADO",
        HoraProceso="09",
        HoraIntervalo="09-10 hrs",
        Turno="Dia",
        MesProceso="1",
        FechaProduccion=date.today(),
        DiaProceso2=date.today()
    )
