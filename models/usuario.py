
from __future__ import annotations
from typing import List

class Usuario:
    def __init__(self, id:int, nombre:str, rol:str, email:str, telefono:str, zonas_interes:List[int], permisos:List[str]):
        self._id = int(id)
        self._nombre = str(nombre)
        self._rol = str(rol)
        self._email = str(email)
        self._telefono = str(telefono)
        self._zonas_interes = list(zonas_interes or [])
        self._permisos = list(permisos or [])

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
    def rol(self)->str: return self._rol
    @rol.setter
    def rol(self, v:str): self._rol = str(v)

    @property
    def email(self)->str: return self._email
    @email.setter
    def email(self, v:str): self._email = str(v)

    @property
    def telefono(self)->str: return self._telefono
    @telefono.setter
    def telefono(self, v:str): self._telefono = str(v)

    @property
    def zonas_interes(self)->List[int]: return self._zonas_interes
    @zonas_interes.setter
    def zonas_interes(self, v:List[int]): self._zonas_interes = list(v or [])

    @property
    def permisos(self)->List[str]: return self._permisos
    @permisos.setter
    def permisos(self, v:List[str]): self._permisos = list(v or [])

    # Métodos
    def asignar_parcela(self, parcela_id:int):
        if parcela_id not in self._zonas_interes:
            self._zonas_interes.append(int(parcela_id))

    def actualizar_contacto(self, email:str, telefono:str):
        self._email = str(email)
        self._telefono = str(telefono)

    def tiene_permiso(self, accion:str) -> bool:
        permisos_normalizados = {str(p).lower() for p in self._permisos}
        return str(accion).lower() in permisos_normalizados

    # ---- PRUEBAS (comentadas) ----
    # u = Usuario(1,"Luis","admin","a@b.com","3000000",[],["crear","leer"]) 
    # u.asignar_parcela(10); assert 10 in u.zonas_interes
    # assert u.tiene_permiso("crear")
