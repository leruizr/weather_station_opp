
from __future__ import annotations
from typing import List, Optional
from .suelo import Suelo
from .fuente_agua import FuenteAgua

class Parcela:
    def __init__(self, id:int, nombre:str, latitud:float, longitud:float, altitud:float, area_ha:float, descripcion:str, propietario_id:int, suelo:Optional[Suelo]=None, fuentes_agua:Optional[List[FuenteAgua]]=None):
        self._id = int(id)
        self._nombre = str(nombre)
        self._latitud = float(latitud)
        self._longitud = float(longitud)
        self._altitud = float(altitud)
        self._area_ha = float(area_ha)
        self._descripcion = str(descripcion)
        self._propietario_id = int(propietario_id)
        self._suelo = suelo
        self._fuentes_agua = list(fuentes_agua) if fuentes_agua else []

    # Getters / setters
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
    def area_ha(self)->float: return self._area_ha
    @area_ha.setter
    def area_ha(self, v:float): self._area_ha = float(v)

    @property
    def descripcion(self)->str: return self._descripcion
    @descripcion.setter
    def descripcion(self, v:str): self._descripcion = str(v)

    @property
    def propietario_id(self)->int: return self._propietario_id
    @propietario_id.setter
    def propietario_id(self, v:int): self._propietario_id = int(v)

    @property
    def suelo(self)->Optional[Suelo]: return self._suelo
    @suelo.setter
    def suelo(self, v:Optional[Suelo]): self._suelo = v

    @property
    def fuentes_agua(self)->List[FuenteAgua]: return self._fuentes_agua

    # Métodos
    def asignar_suelo(self, suelo:Suelo):
        self._suelo = suelo

    def agregar_fuente_agua(self, fuente:FuenteAgua):
        self._fuentes_agua.append(fuente)

    def listar_fuentes_agua(self):
        return list(self._fuentes_agua)

    # ---- PRUEBAS (comentadas) ----
    # p = Parcela(1, "Parcela A", 6.2, -75.6, 1500, 5.0, "desc", 10)
    # from .fuente_agua import FuenteAgua
    # f = FuenteAgua(1, 1, 6.21, -75.61, "quebrada", {"ph":7})
    # p.agregar_fuente_agua(f); assert len(p.listar_fuentes_agua())==1
