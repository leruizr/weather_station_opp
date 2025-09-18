
from __future__ import annotations
from datetime import date
from typing import Tuple, List

class PrediccionClimatica:
    def __init__(self, id:int, estacion_id:int, fecha_emision:date, variable:str, valor_previsto:float, modelo_usado:str, confiabilidad:float):
        self._id = int(id)
        self._estacion_id = int(estacion_id)
        if not isinstance(fecha_emision, date):
            raise TypeError("fecha_emision debe ser date")
        self._fecha_emision = fecha_emision
        self._variable = str(variable)
        self._valor_previsto = float(valor_previsto)
        self._modelo_usado = str(modelo_usado)
        self._confiabilidad = float(confiabilidad)

    # Getters / setters
    @property
    def id(self)->int: return self._id
    @id.setter
    def id(self, v:int): self._id = int(v)

    @property
    def estacion_id(self)->int: return self._estacion_id
    @estacion_id.setter
    def estacion_id(self, v:int): self._estacion_id = int(v)

    @property
    def fecha_emision(self): return self._fecha_emision
    @fecha_emision.setter
    def fecha_emision(self, v:date):
        from datetime import date as _d
        if not isinstance(v, _d): raise TypeError("fecha_emision debe ser date")
        self._fecha_emision = v

    @property
    def variable(self)->str: return self._variable
    @variable.setter
    def variable(self, v:str): self._variable = str(v)

    @property
    def valor_previsto(self)->float: return self._valor_previsto
    @valor_previsto.setter
    def valor_previsto(self, v:float): self._valor_previsto = float(v)

    @property
    def modelo_usado(self)->str: return self._modelo_usado
    @modelo_usado.setter
    def modelo_usado(self, v:str): self._modelo_usado = str(v)

    @property
    def confiabilidad(self)->float: return self._confiabilidad
    @confiabilidad.setter
    def confiabilidad(self, v:float): self._confiabilidad = float(v)

    # Métodos
    def consultar_por_fecha(self, rango:Tuple[date, date]) -> bool:
        ini, fin = rango
        return ini <= self._fecha_emision <= fin

    def mostrar_resumen(self) -> str:
        return (f"Predicción {self._id} - Estación {self._estacion_id}: {self._variable}≈{self._valor_previsto} "
                f"({self._modelo_usado}, conf={self._confiabilidad}) emitida {self._fecha_emision}")

    # ---- PRUEBAS (comentadas) ----
    # from datetime import date
    # p = PrediccionClimatica(1, 10, date.today(), "lluvia", 12.3, "ARIMA", 0.8)
    # assert p.consultar_por_fecha((date(2020,1,1), date(2100,1,1)))
    # assert "Predicción" in p.mostrar_resumen()
