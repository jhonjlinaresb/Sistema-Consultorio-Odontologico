from datetime import date
from src.modelos.cliente import Cliente
from src.modelos.tipo_atencion import TipoAtencion
from src.modelos.prioridad_atencion import PrioridadAtencion
from src.excepciones.cantidad_invalida_error import CantidadInvalidaError

class Cita:
    def __init__(self, cliente: Cliente, tipo_atencion: TipoAtencion, cantidad: int, prioridad: PrioridadAtencion, fecha: date):
        self.cliente = cliente
        self.tipo_atencion = tipo_atencion
        self.prioridad = prioridad
        self.fecha = fecha

        self.cantidad = self._validar_cantidad(tipo_atencion, cantidad)

    def _validar_cantidad(self, tipo_atencion: TipoAtencion, cantidad: int) -> int:
        if cantidad <= 0:
            raise CantidadInvalidaError("La cantidad debe ser mayor a 0.")

        if tipo_atencion in (TipoAtencion.LIMPIEZA, TipoAtencion.DIAGNOSTICO):
            if cantidad != 1:
                raise CantidadInvalidaError(f"La cantidad para {tipo_atencion.name} debe ser 1.")
            return 1

        return cantidad

    def valor_total_cita(self) -> int:
        valor_unitario = self.cliente._tipo_cliente.obtener_valor_atencion(self.tipo_atencion)
        costo_servicio = valor_unitario * self.cantidad
        return self.cliente._tipo_cliente.valor_cita + costo_servicio