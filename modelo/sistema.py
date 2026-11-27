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
    def consultar_aviones(self) -> list[Avion]:
        return self.aviones.copy()
    def buscar_vuelo(self, codigo: str) -> Vuelo | None:
        for vuelo in self.vuelos:
            if vuelo.codigo == codigo:
                return vuelo
        return None
    def buscar_destino(self, nombre:str) -> Destino | None:
        for destino in self.destinos:
            if destino.nombre== nombre:
                return destino
        return None
    def buscar_avion(self, matricula: str) -> Avion | None:
        for avion in self.aviones:
            if avion.matricula == matricula:
                return avion
        return None
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