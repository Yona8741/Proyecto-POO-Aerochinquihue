#Integrantes: Jonathan Paredes, Vicente Aguero, Benjamin Gonzalez
from modelo.sistema import SistemaAeroChinquihue
from controlador.controlador_vuelos import ControladorVuelos
from vista.vista_consola import VistaConsola

def main():
    destinos, aviones, vuelos = crear_datos_iniciales()
    sistema = SistemaAeroChinquihue(destinos, aviones, vuelos)
    controlador = ControladorVuelos(sistema)
    vista = VistaConsola()

    while True:
        opcion = vista.mostrar_menu()
        if opcion == "1":
            vuelos = controlador.listar_vuelos()
            vista.mostrar_vuelos(vuelos)
        elif opcion == "2":
            destinos = controlador.listar_destinos()
            vista.mostrar_destinos(destinos)
        elif opcion == "3":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")
if __name__ == "__main__":
    main()