from src.modelos.interfaces.i_cliente import ICliente
from src.modelos.tipo_cliente import TipoCliente

class Cliente(ICliente):
    def __init__(self, cedula: int, nombre: str, telefono: int, tipo_cliente: TipoCliente):
        super().__init__(cedula, nombre, telefono)
        self._tipo_cliente = tipo_cliente

    def mostrar_informacion(self):
        return f" Cédula: {self.cedula}, \n Nombre: {self.nombre}, \n Teléfono: {self.telefono}, \n Tipo de cliente: {self._tipo_cliente.value} \n"