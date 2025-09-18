from datetime import datetime, timedelta

import pytest

from models import EstacionMeteorologica, LecturaClimatica


def crear_estacion(capacidad=3):
    estacion = EstacionMeteorologica(
        id=1,
        nombre="EM-1",
        latitud=6.2,
        longitud=-75.6,
        altitud=1500.0,
        tipo="automática",
        capacidad_registro=capacidad,
        activa=True,
    )
    estacion.crear_estacion()
    return estacion


def crear_lectura(identificador: int, instante: datetime) -> LecturaClimatica:
    return LecturaClimatica(
        id=identificador,
        estacion_id=1,
        sensor_id=None,
        fecha_hora=instante,
        temperatura=20.5,
        humedad=60.0,
        fuente="sensor",
        calidad_dato="ok",
    )


def test_registrar_y_filtrar_lecturas():
    estacion = crear_estacion()
    ahora = datetime.now()
    lectura_1 = crear_lectura(1, ahora - timedelta(hours=1))
    lectura_2 = crear_lectura(2, ahora)

    estacion.registrar_lectura(lectura_1)
    estacion.registrar_lectura(lectura_2)

    lecturas = estacion.obtener_lecturas((ahora - timedelta(hours=2), ahora + timedelta(minutes=1)))
    assert [l.id for l in lecturas] == [1, 2]


def test_registrar_lectura_otro_id():
    estacion = crear_estacion()
    lectura = LecturaClimatica(
        id=1,
        estacion_id=999,
        sensor_id=None,
        fecha_hora=datetime.now(),
    )

    with pytest.raises(ValueError):
        estacion.registrar_lectura(lectura)


def test_capacidad_actua_como_fifo():
    estacion = crear_estacion(capacidad=2)
    base = datetime.now()
    estacion.registrar_lectura(crear_lectura(1, base))
    estacion.registrar_lectura(crear_lectura(2, base + timedelta(minutes=1)))
    estacion.registrar_lectura(crear_lectura(3, base + timedelta(minutes=2)))

    lecturas = estacion.obtener_lecturas((base - timedelta(minutes=1), base + timedelta(minutes=3)))
    assert [l.id for l in lecturas] == [2, 3]
