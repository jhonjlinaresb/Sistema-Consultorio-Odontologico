from abc import ABC, abstractmethod

class ICliente(ABC):
    def __init__(self, cedula: int, nombre: str, telefono: int):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono

    def tipo_cliente(self):
        return []

    @abstractmethod
    def mostrar_informacion(self):
        pass
