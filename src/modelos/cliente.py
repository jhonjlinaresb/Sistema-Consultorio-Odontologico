from src.modelos.interfaces.i_cliente import ICliente
from src.modelos.tipo_cliente import TipoCliente

class Cliente(ICliente):
    def __init__(self, cedula: int, nombre: str, telefono: int, tipo_cliente: TipoCliente):
        super().__init__(cedula, nombre, telefono)
        self._tipo_cliente = tipo_cliente

    def mostrar_informacion(self):
        return (
            f"Cédula: {self.cedula}\n"
            f"Nombre: {self.nombre}\n"
            f"Teléfono: {self.telefono}\n"
            f"Tipo de Cliente: {self._tipo_cliente.nombre_tipo}\n"
            f"Valor de la Cita: {self._tipo_cliente.valor_cita}\n"
        )