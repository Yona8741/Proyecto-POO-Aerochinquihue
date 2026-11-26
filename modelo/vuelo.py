from datetime import date, time
from decimal import Decimal
from modelo.destino import Destino
from modelo.avion import Avion
from modelo.estado_vuelo import EstadoVuelo
class Vuelo:
    def __init__(
        self,
        codigo: str,
        destino: Destino,
        avion: Avion,
        fecha: date,
        hora: time,
        estado: EstadoVuelo = EstadoVuelo.PROGRAMADO,
        extraordinario: bool = False) -> None:
#Validación datos entrada
        if not codigo.strip():
            raise ValueError("El código no puede estar vacío.")
        if not isinstance(destino, Destino):
            raise TypeError("El destino debe ser de tipo Destino.")
        if not isinstance(avion, Avion):
            raise TypeError("La aeronave debe ser de tipo Avion.")
        if not isinstance(fecha, date):
            raise TypeError("La fecha debe ser de tipo date.")
        if not isinstance(hora, time):
            raise TypeError("La hora debe ser de tipo time.")
        if not isinstance(estado, EstadoVuelo):
            raise TypeError("El estado debe ser de tipo EstadoVuelo.")
        if not isinstance(extraordinario, bool):
            raise TypeError("Extraordinario debe ser de tipo bool.")
#Inicialización atributos privados
        self.__codigo = codigo
        self.__origen = "La Paloma"
        self.__destino = destino
        self.__avion = avion
        self.__fecha = fecha
        self.__hora = hora
        self.__estado = estado
        self.__extraordinario = extraordinario
        self.__reservas: list[object] = []

#Propiedades de solo lectura
    @property
    def codigo(self) -> str:
        return self.__codigo
    @property
    def origen(self) -> str:
        return self.__origen
    @property
    def destino(self) -> Destino:
        return self.__destino
    @property
    def avion(self) -> Avion:
        return self.__avion
    @property
    def fecha(self) -> date:
        return self.__fecha
    @property
    def hora(self) -> time:
        return self.__hora
    @property
    def estado(self) -> EstadoVuelo:
        return self.__estado
    @property
    def extraordinario(self) -> bool:
        return self.__extraordinario

#disponibilidad de pasajeros
    def asientos_disponibles(self) -> int:
        """Retorna los asientos disponibles antes de gestionar reservas."""
        return self.__avion.obtener_capacidad_pasajeros()
    def asiento_disponible(self, asiento: str) -> bool:
        if not asiento.isascii() or not asiento.isdigit():
            return False
        numero = int(asiento)
        return 1 <= numero <= self.__avion.capacidad_pasajeros

#Métodos disponibilidad de carga
    def carga_disponible_kg(self) -> Decimal:
        """Retorna la capacidad de carga disponible antes de las reservas."""
        return self.__avion.obtener_capacidad_carga_kg()
    def admite_encomienda(self, peso_kg: Decimal) -> bool:
        """Comprueba si existe capacidad para una encomienda."""
        if not peso_kg.is_finite() or peso_kg <= 0:
            return False
        return peso_kg <= self.carga_disponible_kg()

#Gestión de vuelos
    def reprogramar(self, fecha: date, hora: time) -> None:
        """Modifica la fecha y hora de un vuelo."""
        if not isinstance(fecha, date):
            raise TypeError("La fecha debe ser de tipo date.")
        if not isinstance(hora, time):
            raise TypeError("La hora debe ser de tipo time.")
        if self.__estado not in (
            EstadoVuelo.PROGRAMADO,
            EstadoVuelo.REPROGRAMADO):
            raise ValueError("El vuelo no puede ser reprogramado.")
        self.__fecha = fecha
        self.__hora = hora
        self.__estado = EstadoVuelo.REPROGRAMADO
    def agregar_reserva(self, reserva: object) -> bool:
        raise NotImplementedError("La gestión de reservas aún no está implementada.")