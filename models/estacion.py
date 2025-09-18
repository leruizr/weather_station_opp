
from __future__ import annotations
from datetime import datetime
from typing import List, Tuple, Optional
from .sensor import Sensor
from .lectura import LecturaClimatica

class EstacionMeteorologica:
    def __init__(self, id:int, nombre:str, latitud:float, longitud:float, altitud:float, tipo:str, capacidad_registro:int, activa:bool=True, sensores:Optional[List[Sensor]]=None, lecturas:Optional[List[LecturaClimatica]]=None):
        self._id = int(id)
        self._nombre = str(nombre)
        self._latitud = float(latitud)
        self._longitud = float(longitud)
        self._altitud = float(altitud)
        self._tipo = str(tipo)
        self._capacidad_registro = int(capacidad_registro)
        self._activa = bool(activa)
        self._sensores = list(sensores or [])
        self._lecturas = list(lecturas or [])

    # Getters/Setters
    @property
    def id(self)->int: return self._id
    @id.setter
    def id(self, v:int): self._id = int(v)

    @property
    def nombre(self)->str: return self._nombre
    @nombre.setter
    def nombre(self, v:str): self._nombre = str(v)

    @property
    def latitud(self)->float: return self._latitud
    @latitud.setter
    def latitud(self, v:float): self._latitud = float(v)

    @property
    def longitud(self)->float: return self._longitud
    @longitud.setter
    def longitud(self, v:float): self._longitud = float(v)

    @property
    def altitud(self)->float: return self._altitud
    @altitud.setter
    def altitud(self, v:float): self._altitud = float(v)

    @property
    def tipo(self)->str: return self._tipo
    @tipo.setter
    def tipo(self, v:str): self._tipo = str(v)

    @property
    def capacidad_registro(self)->int: return self._capacidad_registro
    @capacidad_registro.setter
    def capacidad_registro(self, v:int): self._capacidad_registro = int(v)

    @property
    def activa(self)->bool: return self._activa
    @activa.setter
    def activa(self, v:bool): self._activa = bool(v)

    @property
    def sensores(self)->List[Sensor]: return self._sensores
    @sensores.setter
    def sensores(self, v:List[Sensor]): self._sensores = list(v or [])

    @property
    def lecturas(self)->List[LecturaClimatica]: return self._lecturas
    @lecturas.setter
    def lecturas(self, v:List[LecturaClimatica]): self._lecturas = list(v or [])

    # Métodos CRUD estación
    def crear_estacion(self): 
        # En un sistema real persistiría en BD; aquí sólo valida estado.
        if self._capacidad_registro <= 0:
            raise ValueError("capacidad_registro debe ser > 0")
        self._activa = True
        return True

    def actualizar_estacion(self, **kwargs):
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)
        return True

    def eliminar_estacion(self):
        self._activa = False
        self._sensores.clear()
        self._lecturas.clear()
        return True

    # Gestión de sensores (asignada aquí)
    def agregar_sensor(self, sensor:Sensor):
        if any(s.id == sensor.id for s in self._sensores):
            raise ValueError("ID de sensor duplicado en la estación")
        self._sensores.append(sensor)

    def quitar_sensor(self, id_sensor:int):
        self._sensores = [s for s in self._sensores if s.id != int(id_sensor)]

    def listar_sensores(self):
        return [s.descripcion() for s in self._sensores]

    # Lecturas
    def registrar_lectura(self, lectura:LecturaClimatica):
        if len(self._lecturas) >= self._capacidad_registro:
            self._lecturas.pop(0)  # FIFO
        if lectura.estacion_id != self._id:
            raise ValueError("La lectura pertenece a otra estación")
        self._lecturas.append(lectura)

    def obtener_lecturas(self, rango_fechas:Tuple[datetime, datetime]):
        ini, fin = rango_fechas
        return [l for l in self._lecturas if ini <= l.fecha_hora <= fin]

    def estado(self)->str:
        return f"Estación {self._id} {'activa' if self._activa else 'inactiva'} con {len(self._sensores)} sensores y {len(self._lecturas)} lecturas."

    # ---- PRUEBAS (comentadas) ----
    # from datetime import datetime, timedelta
    # from .sensor import SensorTemperatura
    # from .lectura import LecturaClimatica
    # e = EstacionMeteorologica(1,"EM-1",6.2,-75.6,1500,"automática",3,True)
    # e.crear_estacion()
    # e.agregar_sensor(SensorTemperatura(id=1, precision=0.1, rango_min=-40, rango_max=85, estacion_id=1))
    # now = datetime.now()
    # l = LecturaClimatica(1,1,None,now,temperatura=25.0,fuente="sensor",calidad_dato="ok")
    # e.registrar_lectura(l)
    # assert len(e.obtener_lecturas((now, now)))==1
