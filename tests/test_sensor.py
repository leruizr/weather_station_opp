import pytest

from models import SensorTemperatura


def test_sensor_temperatura_descripcion_y_calibracion():
    sensor = SensorTemperatura(id=1, precision=0.2, rango_min=-50, rango_max=60, estacion_id=1)
    assert "SensorTemperatura" in sensor.descripcion()
    assert sensor.valor_en_rango(0.0) is True

    sensor.calibrar(0.05)
    assert sensor.precision == pytest.approx(0.05)


def test_sensor_valida_rangos_incorrectos():
    with pytest.raises(ValueError):
        SensorTemperatura(id=1, precision=0.1, rango_min=10, rango_max=5, estacion_id=1)


@pytest.mark.parametrize("nuevo_valor", [0, -0.1])
def test_calibrar_rechaza_precision_no_positiva(nuevo_valor):
    sensor = SensorTemperatura(id=2, precision=0.2, rango_min=-10, rango_max=40, estacion_id=1)
    with pytest.raises(ValueError):
        sensor.calibrar(nuevo_valor)
