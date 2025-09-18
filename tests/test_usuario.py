from models import Usuario


def test_asignar_parcela_y_actualizar_contacto():
    usuario = Usuario(
        id=1,
        nombre="Laura",
        rol="analista",
        email="laura@demo.com",
        telefono="3001234567",
        zonas_interes=[],
        permisos=["ver"],
    )

    usuario.asignar_parcela(10)
    usuario.actualizar_contacto("nuevo@demo.com", "3010000000")

    assert 10 in usuario.zonas_interes
    assert usuario.email == "nuevo@demo.com"
    assert usuario.telefono == "3010000000"


def test_tiene_permiso_no_depende_de_mayusculas():
    usuario = Usuario(
        id=2,
        nombre="Carlos",
        rol="admin",
        email="carlos@demo.com",
        telefono="3000000000",
        zonas_interes=[],
        permisos=["Crear", "Listar"],
    )

    assert usuario.tiene_permiso("crear")
    assert usuario.tiene_permiso("CREAR")
    assert not usuario.tiene_permiso("eliminar")
