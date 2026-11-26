from datetime import date, time
from modelo.destino import Destino
from modelo.avion import Avion, Cessna310, Cessna208Caravan, LET410UVPE20
from modelo.vuelo import Vuelo
from modelo.estado_vuelo import EstadoVuelo

def crear_datos_iniciales() -> tuple[list[Destino], list[Avion], list[Vuelo]]:
#destinos y tarifas
    destinos = [
        Destino("Cochamó", 20000, 5000, "Cochamó"),
        Destino("Puelo Bajo", 20000, 5000, "Puelo Bajo"),
        Destino("Contao", 20000, 5000, "Contao"),
        Destino("Río Negro", 25000, 6000, "Río Negro"),
        Destino("Pupelde", 25000, 6000, "Pupelde"),
        Destino("Chepu", 30000, 8000, "Chepu"),
        Destino("Ayacara", 30000, 8000, "Ayacara"),
        Destino("Pillán", 40000, 12000, "Pillán"),
        Destino("Reñihué", 40000, 12000, "Reñihué"),
        Destino("Isla Quenac", 40000, 12000, "Isla Quenac"),
        Destino("Palqui", 40000, 12000, "Palqui"),
        Destino("Chaitén", 50000, 15000, "Chaitén"),
        Destino("Santa Bárbara", 50000, 15000, "Santa Bárbara")]
#Creación de aeronaves con matrículas ficticias
    aviones: list[Avion] = [
        Cessna310("CC-ABC"),
        Cessna208Caravan("CC-DEF"),
        LET410UVPE20("CC-GHI")]
#Fecha vuelos de prueba
    fecha_actual = date.today()
#vuelos ficticios para probar
    vuelos = [
        Vuelo(
            "CHQ-001",
            destinos[0],
            aviones[0],
            fecha_actual,
            time(8, 30),
            EstadoVuelo.PROGRAMADO
        ),
        Vuelo(
            "CHQ-002",
            destinos[5],
            aviones[1],
            fecha_actual,
            time(10, 30),
            EstadoVuelo.PROGRAMADO),
        Vuelo(
            "CHQ-003",
            destinos[11],
            aviones[2],
            fecha_actual,
            time(14, 0),
            EstadoVuelo.PROGRAMADO
        )]
    return destinos, aviones, vuelos