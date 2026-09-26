from src.modelos.interfaces.i_cliente import ICliente

class Cliente(ICliente):
    def __init__(self, cedula: int, nombre: str, telefono: int):
        super().__init__(cedula, nombre, telefono)

    def mostrar_informacion(self):
        return f" Cédula: {self.cedula}, \n Nombre: {self.nombre}, \n Teléfono: {self.telefono} "