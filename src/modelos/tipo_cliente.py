from enum import Enum

class TipoCliente(Enum):
    PARTICULAR =("Particular", 80000)
    EPS =("EPS", 5000)
    PREPAGADA =("Prepagada", 30000)

    def __init__(self, nombre_tipo, valor_cita):
        self.nombre_tipo = nombre_tipo
        self.valor_cita = valor_cita