from datetime import datetime

from models import LecturaClimatica


def test_variables_disponibles_y_validacion():
    lectura = LecturaClimatica(
        id=1,
        estacion_id=10,
        sensor_id=None,
        fecha_hora=datetime(2024, 1, 1, 12, 0),
        temperatura=22.5,
        humedad=55.0,
        precipitacion=3.2,
        viento_vel=5.0,
        viento_dir="N",
        fuente="sensor",
        calidad_dato="validada",
    )

    disponibles = lectura.variables_disponibles()
    assert disponibles == {
        "temperatura": 22.5,
        "humedad": 55.0,
        "precipitacion": 3.2,
        "viento_vel": 5.0,
    }

    assert lectura.validar({
        "temperatura": (0, 40),
        "humedad": (0, 100),
        "precipitacion": (0, 10),
    })
    assert not lectura.validar({"temperatura": (25, 30)})

    linea = lectura.to_csv()
    assert linea.startswith("1,10,")
    assert ",sensor,validada" in linea
