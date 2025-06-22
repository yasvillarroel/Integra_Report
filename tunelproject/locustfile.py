from locust import HttpUser, task, between
import re
import requests
import pandas as pd
from io import BytesIO

class TunelUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        session = requests.Session()

        # Obtener CSRF desde formulario de login
        resp = session.get(self.host + "/")
        csrf_token = re.search(
            r'name="csrfmiddlewaretoken" value="(.+?)"', 
            resp.text
        ).group(1)

        # Hacer POST de login
        login = session.post(self.host + "/", data={
            "username": "testuser",
            "password": "12345",
            "csrfmiddlewaretoken": csrf_token
        }, headers={"Referer": self.host + "/"})

        # Inyectar cookie de sesión a self.client
        if "sessionid" in session.cookies:
            session_id = session.cookies["sessionid"]
            self.client.cookies.set("sessionid", session_id, domain="127.0.0.1")
            print("✅ Login exitoso")
        else:
            print("❌ Login falló. No se obtuvo sessionid")

    @task
    def ver_reportes(self):
        self.client.get("/reportes/?lote=12556&area=Linea+1+Noche&turno=Dia&fecha=2025-01-24&mes_proceso=1&calidad=INDUSTRIAL+A", name="Reportes")

    @task
    def exportar_excel(self):
        self.client.get("/export/excel/?lote=12556&area=Linea+1+Noche&turno=Dia&mes_proceso=1&calidad=INDUSTRIAL+A", name="Excel")

    @task
    def exportar_pdf(self):
        self.client.get("/export/pdf/?lote=12556&area=Linea+1+Noche&turno=Dia&mes_proceso=1&calidad=INDUSTRIAL+A", name="PDF")

    @task
    def ver_estadisticas(self):
        self.client.get("/estadisticas/", name="Estadísticas")

    @task
    def ver_perfil(self):
        self.client.get("/perfil/", name="Perfil")

    @task
    def cargar_archivo(self):
        # 1. Obtener CSRF desde el formulario
        response = self.client.get("/cargar-archivo/")
        csrf_token = re.search(
            r'name="csrfmiddlewaretoken" value="(.+?)"',
            response.text
        ).group(1)

        # 2. Crear archivo Excel en memoria
        df = pd.DataFrame([{
            "diaproceso": "2025-06-21",
            "codigobarra": "000001TEST",
            "lote": "TEST123",
            "area": "Área Test",
            "destinoproducto": "Producto Test",
            "totalkilos": 10.0,
            "totalbandejas": 5,
            "horaproceso": "12:00",
            "horaintervalo": "12-13 hrs",
            "turno": "Día",
            "mesproceso": "6",
            "fechaproduccion": "2025-06-21",
            "diaproceso2": "2025-06-21"
        }])
        buffer = BytesIO()
        df.to_excel(buffer, index=False)
        buffer.seek(0)

        # 3. Enviar el archivo con CSRF en los datos
        files = {
            "archivo_excel": ("test.xlsx", buffer.read(), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        }

        data = {
            "csrfmiddlewaretoken": csrf_token
        }

        self.client.post("/cargar-archivo/", data=data, files=files, headers={
            "Referer": self.client.base_url + "/cargar-archivo/"
        }, name="Cargar archivo")

