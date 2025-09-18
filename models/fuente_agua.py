
from typing import Dict, Any

class FuenteAgua:
    def __init__(self, id:int, parcela_id:int, latitud:float, longitud:float, tipo:str, calidad:Dict[str, Any]):
        self._id = int(id)
        self._parcela_id = int(parcela_id)
        self._latitud = float(latitud)
        self._longitud = float(longitud)
        self._tipo = str(tipo)
        self._calidad = dict(calidad) if calidad is not None else {}

    # Getters / setters
    @property
    def id(self)->int: return self._id
    @id.setter
    def id(self, v:int): self._id = int(v)

    @property
    def parcela_id(self)->int: return self._parcela_id
    @parcela_id.setter
    def parcela_id(self, v:int): self._parcela_id = int(v)

    @property
    def latitud(self)->float: return self._latitud
    @latitud.setter
    def latitud(self, v:float): self._latitud = float(v)

    @property
    def longitud(self)->float: return self._longitud
    @longitud.setter
    def longitud(self, v:float): self._longitud = float(v)

    @property
    def tipo(self)->str: return self._tipo
    @tipo.setter
    def tipo(self, v:str): self._tipo = str(v)

    @property
    def calidad(self)->Dict[str, Any]: return self._calidad
    @calidad.setter
    def calidad(self, v:Dict[str, Any]): self._calidad = dict(v)

    def es_apta_para_riego(self, criterios:Dict[str, Any]) -> bool:
        # Ejemplo simple: verifica que cada clave cumpla rango min/max
        for k, rng in criterios.items():
            if k not in self._calidad: 
                return False
            val = self._calidad[k]
            if isinstance(rng, (list, tuple)) and len(rng)==2:
                if not (rng[0] <= val <= rng[1]):
                    return False
            elif callable(rng):
                if not rng(val): 
                    return False
        return True

    # ---- PRUEBAS (comentadas) ----
    # f = FuenteAgua(1,1,6.2,-75.6,"pozo",{"ph":7})
    # assert f.es_apta_para_riego({"ph":(6,8)})
