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

# etiquetas/tests/conftest.py
import pytest
from django.contrib.auth.models import User
from etiquetas.models import Usuario, RolUser

@pytest.fixture
def usuario_completo(db):
    rol = RolUser.objects.create(id_rol=21, nom_rol="admin")
    user_django = User.objects.create_user(username="adminuser", password="adminpass", email="admin@test.com")
    user_personal = Usuario.objects.create(
        nombre_user="adminuser",
        apellido_user="Tester",
        email_user="admin@test.com",
        pass_user="adminpass",
        id_rol=rol
    )
    return user_django, user_personal