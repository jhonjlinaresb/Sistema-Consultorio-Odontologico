from abc import ABC, abstractmethod

class ICliente(ABC):
    def __init__(self, cedula: int, nombre: str, telefono: int):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono

    @abstractmethod
    def mostrar_informacion(self):
        pass