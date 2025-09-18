
from __future__ import annotations
from typing import Optional, Dict, Any, Tuple, List
from datetime import datetime

class LecturaClimatica:
    """Representa una lectura (posiblemente multivariable) de la estación.

    Atributos:
        id: int
        estacion_id: int
        sensor_id: Optional[int]
        fecha_hora: datetime
        temperatura: Optional[float]
        humedad: Optional[float]
        precipitacion: Optional[float]
        viento_vel: Optional[float]
        viento_dir: Optional[str]
        fuente: str
        calidad_dato: str
    """
    def __init__(self, id:int, estacion_id:int, sensor_id:Optional[int], fecha_hora:datetime,
                 temperatura:Optional[float]=None, humedad:Optional[float]=None, 
                 precipitacion:Optional[float]=None, viento_vel:Optional[float]=None, 
                 viento_dir:Optional[str]=None, fuente:str="manual", calidad_dato:str="bruta"):
        self._id = int(id)
        self._estacion_id = int(estacion_id)
        self._sensor_id = int(sensor_id) if sensor_id is not None else None
        if not isinstance(fecha_hora, datetime):
            raise TypeError("fecha_hora debe ser datetime")
        self._fecha_hora = fecha_hora
        self._temperatura = temperatura
        self._humedad = humedad
        self._precipitacion = precipitacion
        self._viento_vel = viento_vel
        self._viento_dir = viento_dir
        self._fuente = str(fuente)
        self._calidad_dato = str(calidad_dato)

    # Propiedades (getters/setters)
    @property
    def id(self)->int: return self._id
    @id.setter
    def id(self, v:int): self._id = int(v)

    @property
    def estacion_id(self)->int: return self._estacion_id
    @estacion_id.setter
    def estacion_id(self, v:int): self._estacion_id = int(v)

    @property
    def sensor_id(self)->Optional[int]: return self._sensor_id
    @sensor_id.setter
    def sensor_id(self, v:Optional[int]): self._sensor_id = int(v) if v is not None else None

    @property
    def fecha_hora(self)->datetime: return self._fecha_hora
    @fecha_hora.setter
    def fecha_hora(self, v:datetime):
        if not isinstance(v, datetime): raise TypeError("fecha_hora debe ser datetime")
        self._fecha_hora = v

    @property
    def temperatura(self)->Optional[float]: return self._temperatura
    @temperatura.setter
    def temperatura(self, v:Optional[float]): self._temperatura = float(v) if v is not None else None

    @property
    def humedad(self)->Optional[float]: return self._humedad
    @humedad.setter
    def humedad(self, v:Optional[float]): self._humedad = float(v) if v is not None else None

    @property
    def precipitacion(self)->Optional[float]: return self._precipitacion
    @precipitacion.setter
    def precipitacion(self, v:Optional[float]): self._precipitacion = float(v) if v is not None else None

    @property
    def viento_vel(self)->Optional[float]: return self._viento_vel
    @viento_vel.setter
    def viento_vel(self, v:Optional[float]): self._viento_vel = float(v) if v is not None else None

    @property
    def viento_dir(self)->Optional[str]: return self._viento_dir
    @viento_dir.setter
    def viento_dir(self, v:Optional[str]): self._viento_dir = str(v) if v is not None else None

    @property
    def fuente(self)->str: return self._fuente
    @fuente.setter
    def fuente(self, v:str): self._fuente = str(v)

    @property
    def calidad_dato(self)->str: return self._calidad_dato
    @calidad_dato.setter
    def calidad_dato(self, v:str): self._calidad_dato = str(v)

    # Métodos
    def variables_disponibles(self) -> Dict[str, float]:
        """Devuelve un dict con sólo las variables presentes (no None)."""
        data = {
            "temperatura": self._temperatura,
            "humedad": self._humedad,
            "precipitacion": self._precipitacion,
            "viento_vel": self._viento_vel,
        }
        return {k: float(v) for k, v in data.items() if v is not None}

    def validar(self, rangos:Dict[str, Tuple[float, float]]) -> bool:
        """Valida cada variable contra un rango (min,max) provisto."""
        for var, (mn, mx) in rangos.items():
            val = getattr(self, var, None)
            if val is None: 
                continue
            if not (mn <= float(val) <= mx):
                return False
        return True

    def to_csv(self) -> str:
        """Retorna una línea CSV simple con las variables principales."""
        vals = [
            str(self._id), str(self._estacion_id), str(self._sensor_id if self._sensor_id is not None else ""),
            self._fecha_hora.isoformat(),
            "" if self._temperatura is None else str(self._temperatura),
            "" if self._humedad is None else str(self._humedad),
            "" if self._precipitacion is None else str(self._precipitacion),
            "" if self._viento_vel is None else str(self._viento_vel),
            self._viento_dir or "",
            self._fuente, self._calidad_dato
        ]
        return ",".join(vals)

    # ---- PRUEBAS (comentadas) ----
    # from datetime import datetime
    # l = LecturaClimatica(1, 100, None, datetime.now(), temperatura=22.5, humedad=55.0, fuente="sensor", calidad_dato="validada")
    # assert "temperatura" in l.variables_disponibles()
    # assert l.validar({"temperatura":(-50,60)})
    # assert "," in l.to_csv()
