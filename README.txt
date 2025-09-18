
PROYECTO: Sistema de Estación Meteorológica (POO - Python)
==========================================================

Requisitos:
- Clases: EstacionMeteorologica, Sensor (abstracta) + subclases, LecturaClimatica, Parcela, Suelo,
  FuenteAgua, PrediccionClimatica, Usuario.
- Getters y setters vía @property en TODOS los atributos.
- Encapsulamiento, herencia y polimorfismo (sensores).
- Manejo de excepciones y validaciones básicas.
- Pruebas unitarias mínimas como COMENTARIOS al final de cada archivo de clase.
- main.py con menú de texto que permite gestionar estaciones, sensores, lecturas, parcelas/suelos,
  fuentes de agua (vía Parcela), predicciones y usuarios.
- Estructura modular en /models.

Requisitos previos:
- Python 3.10+

Ejecución:
1) Ejecuta:  python main.py
2) Sigue el menú interactivo.

Notas:
- Persistencia: se usa almacenamiento en memoria (diccionarios). Para una entrega académica es suficiente.
- Validaciones: se incluyen validaciones básicas; amplíalas si tu rúbrica lo exige.
- Pruebas: copia/pega los bloques comentados y ejecútalos donde prefieras (o conviértelos en unittest/pytest).
