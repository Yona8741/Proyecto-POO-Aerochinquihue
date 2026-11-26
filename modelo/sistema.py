from datetime import date
from modelo.destino import Destino
from modelo.avion import Avion
from modelo.vuelo import Vuelo

class SistemaAeroChinquihue:
    def __init__(
        self,
        destinos: list[Destino],
        aviones: list[Avion],
        vuelos: list[Vuelo]
    ):
        self.destinos = destinos.copy()
        self.aviones = aviones.copy()
        self.vuelos = vuelos.copy()
    def consultar_vuelos(self, fecha: date | None = None) -> list[Vuelo]:
        if fecha is None:
            return self.vuelos.copy()
        resultado = []
        for vuelo in self.vuelos:
            if vuelo.fecha == fecha:
                resultado.append(vuelo)
        return resultado
    def consultar_destinos(self) -> list[Destino]:
        return self.destinos.copy()
    def registrar_vuelo(self, vuelo: Vuelo) -> bool:
        if vuelo.destino not in self.destinos:
            return False
        if vuelo.avion not in self.aviones:
            return False
        for vuelo_existente in self.vuelos:
            if vuelo_existente.codigo == vuelo.codigo:
                return False
        self.vuelos.append(vuelo)
        return True