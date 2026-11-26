from decimal import Decimal, ROUND_HALF_UP
class Destino:
    def __init__(
        self,
        nombre: str,
        precio_pasaje_clp: int,
        precio_encomienda_kg_clp: int,
        aerodromo_retiro: str
    ) -> None:
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if precio_pasaje_clp <= 0:
            raise ValueError("El precio del pasaje debe ser positivo.")
        if precio_encomienda_kg_clp <= 0:
            raise ValueError("La tarifa de encomienda debe ser positiva.")
        if not aerodromo_retiro.strip():
            raise ValueError("El aeródromo no puede estar vacío.")
        
        self.__nombre = nombre
        self.__precio_pasaje_clp = precio_pasaje_clp
        self.__precio_encomienda_kg_clp = precio_encomienda_kg_clp
        self.__aerodromo_retiro = aerodromo_retiro
        
#Propiedades de solo lectura
    @property
    def nombre(self) -> str:
        return self.__nombre
    @property
    def precio_pasaje_clp(self) -> int:
        return self.__precio_pasaje_clp
    @property
    def precio_encomienda_kg_clp(self) -> int:
        return self.__precio_encomienda_kg_clp
    @property
    def aerodromo_retiro(self) -> str:
        return self.__aerodromo_retiro
    
#metodos del negocio
    def obtener_precio_pasaje(self) -> int:
        return self.__precio_pasaje_clp
    def calcular_costo_encomienda(self, peso_kg: Decimal) -> int:
        if not peso_kg.is_finite() or peso_kg <= 0:
            raise ValueError("El peso debe ser positivo y finito.")
        costo = peso_kg * self.__precio_encomienda_kg_clp
        return int(costo.quantize(Decimal("1"), rounding=ROUND_HALF_UP))