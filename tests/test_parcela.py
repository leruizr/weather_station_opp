from models import FuenteAgua, Parcela, Suelo


def test_asignar_suelo_y_fuentes():
    parcela = Parcela(
        id=1,
        nombre="Parcela A",
        latitud=6.2,
        longitud=-75.6,
        altitud=1500.0,
        area_ha=5.0,
        descripcion="Zona fértil",
        propietario_id=10,
    )

    suelo = Suelo(
        id=1,
        parcela_id=1,
        ph=6.5,
        nutrientes="NPK medio",
        textura="franco",
        materia_organica=2.0,
        clasificacion="A",
    )

    parcela.asignar_suelo(suelo)
    assert parcela.suelo is suelo

    fuente = FuenteAgua(
        id=1,
        parcela_id=1,
        latitud=6.21,
        longitud=-75.61,
        tipo="quebrada",
        calidad={"ph": 7.0},
    )

    parcela.agregar_fuente_agua(fuente)
    assert parcela.listar_fuentes_agua() == [fuente]



def test_suelo_es_apto_por_parametros_basicos():
    suelo = Suelo(
        id=2,
        parcela_id=1,
        ph=6.2,
        nutrientes="rico",
        textura="franco",
        materia_organica=1.8,
        clasificacion="A",
    )
    assert suelo.es_apto("maíz")

    suelo.ph = 8.5
    assert not suelo.es_apto("maíz")



def test_fuente_agua_evalua_criterios():
    fuente = FuenteAgua(
        id=3,
        parcela_id=1,
        latitud=6.22,
        longitud=-75.62,
        tipo="pozo",
        calidad={"ph": 7.2, "conductividad": 1.1},
    )

    assert fuente.es_apta_para_riego({"ph": (6.5, 7.5)})
    assert not fuente.es_apta_para_riego({"conductividad": (0, 1)})
