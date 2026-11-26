from modelo.vuelo import Vuelo
from modelo.destino import Destino
class VistaConsola:
    def mostrar_menu(self) -> str:
        print("\nAeroChinquihue")
        print("1. Consultar vuelos")
        print("2. Consultar destinos")
        print("3. Salir")
        return input("Seleccione una opción: ")

    def mostrar_vuelos(self, vuelos: list[Vuelo]) -> None:
        print("\nLista de vuelos")
        if not vuelos:
            print("No hay vuelos disponibles.")
            return
        for vuelo in vuelos:
            print(f"\nCódigo: {vuelo.codigo}")
            print(f"Origen: {vuelo.origen}")
            print(f"Destino: {vuelo.destino.nombre}")
            print(f"Aeronave: {vuelo.avion.modelo}")
            print(f"Fecha: {vuelo.fecha}")
            print(f"Hora: {vuelo.hora}")
            print(f"Estado: {vuelo.estado.name}")
            print(f"Asientos disponibles: {vuelo.asientos_disponibles()}")
            print(f"Carga disponible: {vuelo.carga_disponible_kg()} kg")

    def mostrar_destinos(self, destinos: list[Destino]) -> None:
        print("\nLista de destinos")
        if not destinos:
            print("No hay destinos disponibles.")
            return
        for destino in destinos:
            print(f"\nDestino: {destino.nombre}")
            print(f"Precio del pasaje: ${destino.precio_pasaje_clp}")
            print(f"Encomienda por kg: ${destino.precio_encomienda_kg_clp}")
            print(f"Lugar de retiro: {destino.aerodromo_retiro}")