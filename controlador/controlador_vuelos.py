from datetime import date
from modelo.sistema import SistemaAeroChinquihue
from modelo.vuelo import Vuelo
from modelo.destino import Destino
from modelo.avion import Avion

class ControladorVuelos:
    def __init__(self, sistema: SistemaAeroChinquihue):
        self.sistema = sistema
    def listar_vuelos(self, fecha: date | None = None) -> list[Vuelo]:
        return self.sistema.consultar_vuelos(fecha)
    def listar_destinos(self) -> list[Destino]:
        return self.sistema.consultar_destinos()
    def listar_aviones(self) -> list[Avion]:
        return self.sistema.consultar_aviones()
    def buscar_vuelo (self, codigo: str) -> Vuelo | None:
        return self.sistema.buscar_vuelo(codigo)
    def buscar_destino(self, nombre: str) -> Destino | None:
        return self.sistema.buscar_destino(nombre)
    def buscar_avion(self, matricula: str) -> Avion | None:
        return self.sistema.buscar_avion(matricula)
    def registrar_vuelo(self, vuelo: Vuelo) -> bool:
        return self.sistema.registrar_vuelo(vuelo)