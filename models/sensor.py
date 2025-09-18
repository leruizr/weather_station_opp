
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

class Sensor(ABC):
    """Clase abstracta Sensor.

    Atributos:
        id (int)
        tipo (str)
        unidad (str)
        precision (float)
        rango_min (float)
        rango_max (float)
        estacion_id (int)
        estado (bool)

    Métodos abstractos comunes y utilitarios.
    NOTA DE PRUEBAS (comentadas al final del archivo).
    """
    def __init__(self, id:int, tipo:str, unidad:str, precision:float, rango_min:float, rango_max:float, estacion_id:int, estado:bool=True):
        self._id = int(id)
        self._tipo = str(tipo)
        self._unidad = str(unidad)
        self._precision = float(precision)
        self._rango_min = float(rango_min)
        self._rango_max = float(rango_max)
        if self._rango_min > self._rango_max:
            raise ValueError("rango_min no puede ser mayor que rango_max")
        self._estacion_id = int(estacion_id)
        self._estado = bool(estado)

    # Getters & Setters (propiedades)
    @property
    def id(self)->int: return self._id
    @id.setter
    def id(self, value:int): self._id = int(value)

    @property
    def tipo(self)->str: return self._tipo
    @tipo.setter
    def tipo(self, value:str): self._tipo = str(value)

    @property
    def unidad(self)->str: return self._unidad
    @unidad.setter
    def unidad(self, value:str): self._unidad = str(value)

    @property
    def precision(self)->float: return self._precision
    @precision.setter
    def precision(self, value:float):
        v = float(value)
        if v <= 0: raise ValueError("precision debe ser > 0")
        self._precision = v

    @property
    def rango_min(self)->float: return self._rango_min
    @rango_min.setter
    def rango_min(self, value:float):
        v = float(value)
        if v > self._rango_max:
            raise ValueError("rango_min no puede ser mayor que rango_max")
        self._rango_min = v

    @property
    def rango_max(self)->float: return self._rango_max
    @rango_max.setter
    def rango_max(self, value:float):
        v = float(value)
        if v < self._rango_min:
            raise ValueError("rango_max no puede ser menor que rango_min")
        self._rango_max = v

    @property
    def estacion_id(self)->int: return self._estacion_id
    @estacion_id.setter
    def estacion_id(self, value:int): self._estacion_id = int(value)

    @property
    def estado(self)->bool: return self._estado
    @estado.setter
    def estado(self, value:bool): self._estado = bool(value)

    # Métodos requeridos (ubicados aquí por especificación del enunciado)
    @abstractmethod
    def descripcion(self) -> str:
        """Descripción del sensor."""

    # Métodos de gestión (la especificación los nombra en Sensor; se implementan en Estacion)
    def agregar_sensor(self, sensor:'Sensor'):
        raise NotImplementedError("agregar_sensor() se gestiona en EstacionMeteorologica")

    def quitar_sensor(self, id_sensor:int):
        raise NotImplementedError("quitar_sensor() se gestiona en EstacionMeteorologica")

    def calibrar(self, nueva_precision:float):
        self.precision = nueva_precision
        return self._precision

    # Utilidad de validación de rango
    def valor_en_rango(self, v:float) -> bool:
        return self._rango_min <= float(v) <= self._rango_max

class SensorTemperatura(Sensor):
    def __init__(self, **kwargs):
        kwargs.setdefault("tipo", "temperatura")
        kwargs.setdefault("unidad", "°C")
        super().__init__(**kwargs)
    def descripcion(self)->str:
        return f"SensorTemperatura(id={self.id}, unidad={self.unidad}, precisión={self.precision})"

class SensorHumedad(Sensor):
    def __init__(self, **kwargs):
        kwargs.setdefault("tipo", "humedad")
        kwargs.setdefault("unidad", "%")
        super().__init__(**kwargs)
    def descripcion(self)->str:
        return f"SensorHumedad(id={self.id}, unidad={self.unidad}, precisión={self.precision})"

class SensorPrecipitacion(Sensor):
    def __init__(self, **kwargs):
        kwargs.setdefault("tipo", "precipitacion")
        kwargs.setdefault("unidad", "mm")
        super().__init__(**kwargs)
    def descripcion(self)->str:
        return f"SensorPrecipitacion(id={self.id}, unidad={self.unidad}, precisión={self.precision})"

class SensorViento(Sensor):
    def __init__(self, **kwargs):
        kwargs.setdefault("tipo", "viento")
        kwargs.setdefault("unidad", "m/s")
        super().__init__(**kwargs)
    def descripcion(self)->str:
        return f"SensorViento(id={self.id}, unidad={self.unidad}, precisión={self.precision})"

# ---- PRUEBAS (comentadas) ----
# s = SensorTemperatura(id=1, unidad="°C", precision=0.1, rango_min=-40, rango_max=85, estacion_id=100)
# assert s.valor_en_rango(20.0) is True
# assert s.descripcion().startswith("SensorTemperatura")
# s.calibrar(0.05); assert s.precision == 0.05
