from datetime import date
from modelo.sistema import SistemaAeroChinquihue
from modelo.vuelo import Vuelo
from modelo.destino import Destino

class ControladorVuelos:
    def __init__(self, sistema: SistemaAeroChinquihue):
        self.sistema = sistema
    def listar_vuelos(self, fecha: date | None = None) -> list[Vuelo]:
        return self.sistema.consultar_vuelos(fecha)
    def listar_destinos(self) -> list[Destino]:
        return self.sistema.consultar_destinos()
    def registrar_vuelo(self, vuelo: Vuelo) -> bool:
        return self.sistema.registrar_vuelo(vuelo)