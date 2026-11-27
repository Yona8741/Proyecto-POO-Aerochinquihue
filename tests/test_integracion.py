from datetime import date, time
from datos.datos_iniciales import crear_datos_iniciales
from modelo.sistema import SistemaAeroChinquihue
from modelo.vuelo import Vuelo
from controlador.controlador_vuelos import ControladorVuelos

def test_consultar_destinos():
    destinos, aviones, vuelos = crear_datos_iniciales()
    sistema = SistemaAeroChinquihue(destinos, aviones, vuelos)
    assert sistema.consultar_destinos() == destinos
    assert len(sistema.consultar_destinos()) == 13
def test_consultar_vuelos():
    destinos, aviones, vuelos = crear_datos_iniciales()
    sistema = SistemaAeroChinquihue(destinos, aviones, vuelos)
    assert sistema.consultar_vuelos() == vuelos
def test_consultar_vuelos_por_fecha():
    destinos, aviones, vuelos = crear_datos_iniciales()
    sistema = SistemaAeroChinquihue(destinos, aviones, vuelos)
    fecha = vuelos[0].fecha
    resultado = sistema.consultar_vuelos(fecha)
    assert len(resultado) > 0
    assert all(vuelo.fecha == fecha for vuelo in resultado)
def test_registrar_vuelo():
    destinos, aviones, vuelos = crear_datos_iniciales()
    sistema = SistemaAeroChinquihue(destinos, aviones, vuelos)
    vuelo = Vuelo(
        "TEST-001",
        destinos[0],
        aviones[0],
        date.today(),
        time(12, 0))
    assert sistema.registrar_vuelo(vuelo) is True
    assert vuelo in sistema.consultar_vuelos()
def test_vuelo_duplicado():
    destinos, aviones, vuelos = crear_datos_iniciales()
    sistema = SistemaAeroChinquihue(destinos, aviones, vuelos)
    assert sistema.registrar_vuelo(vuelos[0]) is False
def test_controlador():
    destinos, aviones, vuelos = crear_datos_iniciales()
    sistema = SistemaAeroChinquihue(destinos, aviones, vuelos)
    controlador = ControladorVuelos(sistema)
    assert controlador.listar_destinos() == destinos
    assert controlador.listar_vuelos() == vuelos
def test_sistema_vacio():
    sistema = SistemaAeroChinquihue([], [], [])
    assert sistema.consultar_destinos() == []
    assert sistema.consultar_vuelos() == []
    
    
def test_listar_aviones():
    destinos, aviones, vuelos = crear_datos_iniciales()
    sistema = SistemaAeroChinquihue(destinos, aviones, vuelos)
    controlador = ControladorVuelos(sistema)

    assert controlador.listar_aviones() == aviones


def test_buscar_vuelo():
    destinos, aviones, vuelos = crear_datos_iniciales()
    sistema = SistemaAeroChinquihue(destinos, aviones, vuelos)
    controlador = ControladorVuelos(sistema)

    assert controlador.buscar_vuelo("CHQ-002") is vuelos[1]
    assert controlador.buscar_vuelo("INEXISTENTE") is None


def test_buscar_destino():
    destinos, aviones, vuelos = crear_datos_iniciales()
    sistema = SistemaAeroChinquihue(destinos, aviones, vuelos)
    controlador = ControladorVuelos(sistema)

    assert controlador.buscar_destino("Chepu") is destinos[5]
    assert controlador.buscar_destino("INEXISTENTE") is None


def test_buscar_avion():
    destinos, aviones, vuelos = crear_datos_iniciales()
    sistema = SistemaAeroChinquihue(destinos, aviones, vuelos)
    controlador = ControladorVuelos(sistema)

    assert controlador.buscar_avion("CC-DEF") is aviones[1]
    assert controlador.buscar_avion("INEXISTENTE") is None
