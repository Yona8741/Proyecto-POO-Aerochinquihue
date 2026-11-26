from abc import ABC, abstractmethod
from decimal import Decimal
class Avion(ABC):
    @abstractmethod
    def __init__(
        self,
        matricula: str,
        modelo: str,
        capacidad_pasajeros: int,
        capacidad_carga_kg: Decimal
    ) -> None:
#Validación de los datos de entrada
        if not matricula.strip():
            raise ValueError("La matrícula no puede estar vacía.")
        if not modelo.strip():
            raise ValueError("El modelo no puede estar vacío.")
        if capacidad_pasajeros <= 0:
            raise ValueError("La capacidad de pasajeros debe ser positiva.")
        if not capacidad_carga_kg.is_finite() or capacidad_carga_kg <= 0:
            raise ValueError("La capacidad de carga debe ser positiva y finita.")

#Inicialización de atributos privados
        self.__matricula = matricula
        self.__modelo = modelo
        self.__capacidad_pasajeros = capacidad_pasajeros
        self.__capacidad_carga_kg = capacidad_carga_kg

#Propiedades de solo lectura
    @property
    def matricula(self) -> str:
        return self.__matricula
    @property
    def modelo(self) -> str:
        return self.__modelo
    @property
    def capacidad_pasajeros(self) -> int:
        return self.__capacidad_pasajeros
    @property
    def capacidad_carga_kg(self) -> Decimal:
        return self.__capacidad_carga_kg
#Metodos de negocio
    def obtener_capacidad_pasajeros(self) -> int:
        return self.__capacidad_pasajeros
    def obtener_capacidad_carga_kg(self) -> Decimal:
        return self.__capacidad_carga_kg

class Cessna310(Avion):
    CAPACIDAD_PASAJEROS = 5
    CAPACIDAD_CARGA_KG = Decimal("910")

    def __init__(self, matricula: str) -> None:
        super().__init__(
            matricula,
            "Cessna 310",
            self.CAPACIDAD_PASAJEROS,
            self.CAPACIDAD_CARGA_KG)
class Cessna208Caravan(Avion):
    CAPACIDAD_PASAJEROS = 9
    CAPACIDAD_CARGA_KG = Decimal("1315")
    def __init__(self, matricula: str) -> None:
        super().__init__(
            matricula,
            "Cessna 208 Caravan",
            self.CAPACIDAD_PASAJEROS,
            self.CAPACIDAD_CARGA_KG
        )

class LET410UVPE20(Avion):
    CAPACIDAD_PASAJEROS = 19
    CAPACIDAD_CARGA_KG = Decimal("1800")

    def __init__(self, matricula: str) -> None:
        super().__init__(
            matricula,
            "LET 410 UVP-E20",
            self.CAPACIDAD_PASAJEROS,
            self.CAPACIDAD_CARGA_KG)