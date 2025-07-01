# Integra_Report

## 📊 Sistema de Gestión de Producción

Este proyecto es un sistema web desarrollado como parte de un proyecto académico, enfocado en mejorar la visualización y gestión de datos productivos para el área de control de producción de una empresa.

## 🚀 Funcionalidades principales

- Visualización de datos de producción en tiempo real.
- Filtros por fecha y categoría para análisis detallado.
- Exportación de reportes en formato Excel y PDF.
- Gráficos dinámicos (diarios, semanales, mensuales).
- Interfaz amigable y funcional para escritorio.

## 🛠️ Tecnologías utilizadas

- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Backend:** Django REST Framework
- **Gráficos:** Chart.js
- **Base de datos:** MySQL
- **Exportación:** `pandas`, `openpyxl`, `reportlab`

## ⚙️ Instalación y ejecución (sin entorno virtual)

1. Asegúrate de tener Python 3 y pip instalados.
2. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/integra-report.git
   cd integra-report
   ```
3. Instala las dependencias requeridas:
  ```bash
  pip install -r requirements.txt
  ```
4. Configura la base de datos MySQL en el archivo settings.py:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_de_tu_base_de_datos',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
5. Aplica las migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Ejecuta el servidor:
   ```bash
   python manage.py runserver
   ```
7. Abre tu navegador y ve a:
   ```bash
   http://localhost:8000
   ```
## 👤 Autor

- **Nombre:** Yasna Villarroel
- **Carrera:** Analista Programador Computacional
- **Institución:** Duoc UC
