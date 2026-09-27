from enum import Enum
from src.modelos.tipo_atencion import TipoAtencion

class TipoCliente(Enum):
    PARTICULAR =("Particular", 80000, {
        TipoAtencion.LIMPIEZA: 60000,
        TipoAtencion.CALZAS: 80000,
        TipoAtencion.EXTRACCION: 100000,
        TipoAtencion.DIAGNOSTICO: 50000                 
    })
    EPS =("EPS", 5000, {
        TipoAtencion.LIMPIEZA: 0,
        TipoAtencion.CALZAS: 40000,
        TipoAtencion.EXTRACCION: 40000,
        TipoAtencion.DIAGNOSTICO: 0
    })
    PREPAGADA =("Prepagada", 30000, {
        TipoAtencion.LIMPIEZA: 0,
        TipoAtencion.CALZAS: 10000,
        TipoAtencion.EXTRACCION: 10000,
        TipoAtencion.DIAGNOSTICO: 0
    })

    def __init__(self, nombre_tipo: str, valor_cita: int, valor_atencion: dict):
        self.nombre_tipo = nombre_tipo
        self.valor_cita = valor_cita
        self.valor_atencion = valor_atencion

    def obtener_valor_atencion(self, tipo_atencion: TipoAtencion) -> int:
        return self.valor_atencion.get(tipo_atencion, 0)