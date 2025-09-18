from datetime import date, timedelta

from models import PrediccionClimatica


def test_prediccion_consulta_y_resumen():
    hoy = date.today()
    prediccion = PrediccionClimatica(
        id=1,
        estacion_id=5,
        fecha_emision=hoy,
        variable="lluvia",
        valor_previsto=12.3,
        modelo_usado="ARIMA",
        confiabilidad=0.8,
    )

    assert prediccion.consultar_por_fecha((hoy - timedelta(days=1), hoy + timedelta(days=1)))
    assert "Predicción" in prediccion.mostrar_resumen()
