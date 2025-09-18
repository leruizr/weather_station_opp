
class Suelo:
    def __init__(self, id:int, parcela_id:int, ph:float, nutrientes:str, textura:str, materia_organica:float, clasificacion:str):
        self._id = int(id)
        self._parcela_id = int(parcela_id)
        self._ph = float(ph)
        self._nutrientes = str(nutrientes)
        self._textura = str(textura)
        self._materia_organica = float(materia_organica)
        self._clasificacion = str(clasificacion)

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
    def ph(self)->float: return self._ph
    @ph.setter
    def ph(self, v:float): self._ph = float(v)

    @property
    def nutrientes(self)->str: return self._nutrientes
    @nutrientes.setter
    def nutrientes(self, v:str): self._nutrientes = str(v)

    @property
    def textura(self)->str: return self._textura
    @textura.setter
    def textura(self, v:str): self._textura = str(v)

    @property
    def materia_organica(self)->float: return self._materia_organica
    @materia_organica.setter
    def materia_organica(self, v:float): self._materia_organica = float(v)

    @property
    def clasificacion(self)->str: return self._clasificacion
    @clasificacion.setter
    def clasificacion(self, v:str): self._clasificacion = str(v)

    def es_apto(self, cultivo:str)->bool:
        # Criterio muy simple de ejemplo
        return 5.5 <= self._ph <= 7.5 and self._materia_organica >= 1.5

    # ---- PRUEBAS (comentadas) ----
    # s = Suelo(1,1,6.5,"NPK medio","franco",2.0,"A"); assert s.es_apto("maiz")
