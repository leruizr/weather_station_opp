
from __future__ import annotations
from datetime import datetime, date
from typing import Dict, List, Optional
from models import (
    EstacionMeteorologica, SensorTemperatura, SensorHumedad, SensorPrecipitacion, SensorViento,
    LecturaClimatica, Parcela, Suelo, FuenteAgua, PrediccionClimatica, Usuario
)

# Repositorios en memoria
estaciones: Dict[int, EstacionMeteorologica] = {}
parcelas: Dict[int, Parcela] = {}
predicciones: Dict[int, PrediccionClimatica] = {}
usuarios: Dict[int, Usuario] = {}

def input_int(msg:str)->int:
    return int(input(msg).strip())
def input_float(msg:str)->float:
    return float(input(msg).strip())
def input_str(msg:str)->str:
    return input(msg).strip()

# ---- ESTACIONES ----
def menu_estaciones():
    while True:
        print("\n[Estaciones] 1.Crear 2.Actualizar 3.Eliminar 4.Listar 5.Gestión Sensores 6.Registrar/Lecturas 0.Volver")
        op = input_str("> ")
        if op == "1":
            try:
                id = input_int("ID: ")
                estaciones[id] = EstacionMeteorologica(
                    id, input_str("Nombre: "), input_float("Latitud: "),
                    input_float("Longitud: ") , input_float("Altitud: "),
                    input_str("Tipo: ") , input_int("Capacidad de registros: ") , True
                )
                estaciones[id].crear_estacion()
                print("Creada.")
            except Exception as e:
                print("Error:", e)
        elif op == "2":
            try:
                id = input_int("ID estación a actualizar: ")
                if id not in estaciones: print("No existe"); continue
                nombre = input_str("Nombre (enter para omitir): ")
                if nombre: estaciones[id].nombre = nombre
                print("Actualizada.")
            except Exception as e:
                print("Error:", e)
        elif op == "3":
            id = input_int("ID estación a eliminar: ")
            if id in estaciones:
                estaciones[id].eliminar_estacion()
                print("Eliminada (inactivada).")
            else:
                print("No existe")
        elif op == "4":
            for e in estaciones.values():
                print(e.estado())
        elif op == "5":
            gestion_sensores()
        elif op == "6":
            lecturas_menu()
        elif op == "0":
            break

def gestion_sensores():
    id = input_int("ID estación: ")
    if id not in estaciones: print("No existe"); return
    est = estaciones[id]
    while True:
        print("[Sensores] 1.Agregar 2.Quitar 3.Calibrar 4.Listar 0.Volver")
        op = input_str("> ")
        if op == "1":
            try:
                sid = input_int("ID sensor: ")
                stipo = input_str("Tipo (t/h/p/v): ")
                kwargs = dict(id=sid, precision=input_float("Precisión:"), rango_min=input_float("Rango min:"), rango_max=input_float("Rango max:"), estacion_id=id)
                s = None
                if stipo == 't': s = SensorTemperatura(**kwargs)
                elif stipo == 'h': s = SensorHumedad(**kwargs)
                elif stipo == 'p': s = SensorPrecipitacion(**kwargs)
                elif stipo == 'v': s = SensorViento(**kwargs)
                else: print("Tipo inválido"); continue
                est.agregar_sensor(s); print("Agregado.")
            except Exception as e:
                print("Error:", e)
        elif op == "2":
            sid = input_int("ID a quitar: "); est.quitar_sensor(sid); print("Quitado.")
        elif op == "3":
            sid = input_int("ID a calibrar: "); nueva = input_float("Nueva precisión: ")
            for s in est.sensores:
                if s.id == sid:
                    s.calibrar(nueva); print("Calibrado."); break
            else:
                print("No existe ese sensor")
        elif op == "4":
            print(*est.listar_sensores(), sep="\n")
        elif op == "0":
            break

def lecturas_menu():
    id = input_int("ID estación: ")
    if id not in estaciones: print("No existe"); return
    est = estaciones[id]
    while True:
        print("[Lecturas] 1.Registrar 2.Consultar por rango 0.Volver")
        op = input_str("> ")
        if op == "1":
            try:
                lid = input_int("ID lectura: ")
                sensor_id = input_str("Sensor ID (vacío si no aplica): ")
                sid = int(sensor_id) if sensor_id else None
                t = input_str("Temp (vacío si no aplica): ")
                h = input_str("Humedad: ")
                p = input_str("Precipitación: ")
                vv = input_str("Viento vel: ")
                vd = input_str("Viento dir: ")
                l = LecturaClimatica(
                    lid, id, sid, datetime.now(),
                    temperatura=float(t) if t else None,
                    humedad=float(h) if h else None,
                    precipitacion=float(p) if p else None,
                    viento_vel=float(vv) if vv else None,
                    viento_dir=vd or None,
                    fuente="sensor", calidad_dato="ok")
                est.registrar_lectura(l); print("Registrada.")
            except Exception as e:
                print("Error:", e)
        elif op == "2":
            try:
                ini = input_str("Inicio YYYY-MM-DD: "); fin = input_str("Fin YYYY-MM-DD: ")
                from datetime import datetime as _dt
                r = est.obtener_lecturas((_dt.fromisoformat(ini+" 00:00:00"), _dt.fromisoformat(fin+" 23:59:59")))
                for l in r:
                    print(l.to_csv())
            except Exception as e:
                print("Error:", e)
        elif op == "0":
            break

# ---- PARCELAS y SUELOS ----
def menu_parcelas():
    while True:
        print("\n[Parcelas] 1.Crear 2.Asignar suelo 3.Agregar fuente agua 4.Listar fuentes 0.Volver")
        op = input_str("> ")
        if op == "1":
            id = input_int("ID: ")
            parcelas[id] = Parcela(id, input_str("Nombre:"), input_float("Lat:"), input_float("Lon:"), input_float("Alt:"), input_float("Área ha:"), input_str("Desc:"), input_int("Propietario ID:"))
            print("Creada.")
        elif op == "2":
            id = input_int("ID parcela: ")
            if id not in parcelas: print("No existe"); continue
            s = Suelo(input_int("Suelo ID:"), id, input_float("pH:"), input_str("Nutrientes:"), input_str("Textura:"), input_float("% MO:"), input_str("Clasificación:"))
            parcelas[id].asignar_suelo(s); print("Asignado.")
        elif op == "3":
            id = input_int("ID parcela: ")
            if id not in parcelas: print("No existe"); continue
            f = FuenteAgua(input_int("Fuente ID:"), id, input_float("Lat:"), input_float("Lon:"), input_str("Tipo:"), {"ph": float(input_str("pH agua:"))})
            parcelas[id].agregar_fuente_agua(f); print("Agregada.")
        elif op == "4":
            id = input_int("ID parcela: ")
            if id in parcelas:
                for f in parcelas[id].listar_fuentes_agua(): print(f"Fuente {f.id} tipo {f.tipo}")
            else:
                print("No existe")
        elif op == "0":
            break

# ---- PREDICCIONES ----
def menu_predicciones():
    while True:
        print("\n[Predicciones] 1.Crear 2.Consultar por fecha 3.Listar 0.Volver")
        op = input_str("> ")
        if op == "1":
            id = input_int("ID: ")
            predicciones[id] = PrediccionClimatica(id, input_int("Estación ID:"), date.fromisoformat(input_str("Fecha emision YYYY-MM-DD:")), input_str("Variable:"), float(input_str("Valor previsto:")), input_str("Modelo:"), float(input_str("Confiabilidad 0-1:")))
            print("Creada.")
        elif op == "2":
            ini = date.fromisoformat(input_str("Inicio YYYY-MM-DD:"))
            fin = date.fromisoformat(input_str("Fin YYYY-MM-DD:"))
            for p in predicciones.values():
                if p.consultar_por_fecha((ini, fin)): print(p.mostrar_resumen())
        elif op == "3":
            for p in predicciones.values(): print(p.mostrar_resumen())
        elif op == "0":
            break

# ---- USUARIOS ----
def menu_usuarios():
    while True:
        print("\n[Usuarios] 1.Crear 2.Actualizar contacto 3.Asignar parcela 4.Ver permisos 0.Volver")
        op = input_str("> ")
        if op == "1":
            id = input_int("ID: ")
            usuarios[id] = Usuario(id, input_str("Nombre:"), input_str("Rol:"), input_str("Email:"), input_str("Tel:"), [], input_str("Permisos separados por coma:" ).split(","))
            print("Creado.")
        elif op == "2":
            id = input_int("ID: "); 
            if id in usuarios:
                usuarios[id].actualizar_contacto(input_str("Nuevo email:"), input_str("Nuevo tel:")); print("Actualizado.")
            else:
                print("No existe")
        elif op == "3":
            id = input_int("ID: "); par = input_int("Parcela ID:");
            if id in usuarios:
                usuarios[id].asignar_parcela(par); print("Asignada.")
            else:
                print("No existe")
        elif op == "4":
            id = input_int("ID: "); acc = input_str("Acción a verificar:");
            if id in usuarios:
                print("Tiene permiso?", usuarios[id].tiene_permiso(acc))
            else:
                print("No existe")
        elif op == "0":
            break

def main():
    while True:
        print("\n== Sistema Estación Meteorológica ==")
        print("1. Estaciones  2. Parcelas/Suelo  3. Predicciones  4. Usuarios  0. Salir")
        op = input_str("> ")
        if op == "1": menu_estaciones()
        elif op == "2": menu_parcelas()
        elif op == "3": menu_predicciones()
        elif op == "4": menu_usuarios()
        elif op == "0": break

if __name__ == "__main__":
    main()
