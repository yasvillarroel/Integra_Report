from django.db import models # Importa el módulo de modelos de Django
from django.contrib.auth.models import User # Importa el modelo de usuario de Django

#-------------------------------------------------------------Modelo de etiquetas----------------------------------------------------------------
class RolUser(models.Model):
    id_rol = models.IntegerField(primary_key=True, unique=True)
    nom_rol = models.CharField(max_length=50)

    class Meta:
        db_table = 'rol_user'
        managed = True

    def __str__(self):
        return self.nom_rol

class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    nombre_user = models.CharField(max_length=100)
    apellido_user = models.CharField(max_length=100)
    email_user = models.EmailField(unique=True)
    pass_user = models.CharField(max_length=255)
    id_rol = models.ForeignKey(RolUser, on_delete=models.CASCADE, db_column='id_rol')

    class Meta:
        db_table = 'usuarios'
        managed = True

    
class CargarArchivo(models.Model):
    id_archivo = models.AutoField(primary_key=True)
    nombre_archivo = models.CharField(max_length=200)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_user')

    class Meta:
        db_table = 'cargar_archivo'
        managed = True

    
class Etiqueta(models.Model):
    id_etiqueta = models.AutoField(primary_key=True, db_column='id_etiqueta')
    DiaProceso = models.DateField(db_column='dia_proceso')
    CodigoBarra = models.CharField(max_length=50, db_column='codigo_barra')
    Lote = models.CharField(max_length=50, db_column='lote')
    Area = models.CharField(max_length=50, db_column='area')
    DestinoProducto = models.CharField(max_length=100, db_column='destino_producto')
    TotalKilos = models.DecimalField(max_digits=10, decimal_places=2, db_column='total_kilos')
    TotalBandejas = models.IntegerField(db_column='total_bandejas')
    Corte = models.CharField(max_length=50, null=True, blank=True, db_column='corte')
    Calidad = models.CharField(max_length=50, null=True, blank=True, db_column='calidad')
    Conservacion = models.CharField(max_length=50, null=True, blank=True, db_column='conservacion')
    HoraProceso = models.TimeField(db_column='hora_proceso')
    HoraIntervalo = models.CharField(max_length=20, db_column='hora_intervalo')
    Turno = models.CharField(max_length=20, db_column='turno')
    MesProceso = models.CharField(max_length=20, db_column='mes_proceso')
    FechaProduccion = models.DateField(db_column='fecha_produccion')
    DiaProceso2 = models.DateField(db_column='dia_proceso2')

    archivo_origen = models.ForeignKey(
        CargarArchivo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='id_archivo'
    )

    class Meta:
        db_table = 'etiquetas_tunel'
        managed = True

    def __str__(self):
        return f"{self.DiaProceso} - {self.CodigoBarra}"

    