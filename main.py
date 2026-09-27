from src.modelos.cliente import Cliente
from src.modelos.tipo_cliente import TipoCliente
from src.modelos.tipo_atencion import TipoAtencion

cliente1 = Cliente(123456789, "Juan Perez", 5551234, TipoCliente.PARTICULAR)
cliente2 = Cliente(987654321, "Maria Gomez", 5555678, TipoCliente.EPS)
cliente3 = Cliente(456789123, "Carlos Rodriguez", 5559876, TipoCliente.PREPAGADA)
cliente4 = Cliente(111222333, "Ana Martinez", 5554321, TipoCliente.PARTICULAR)

print(cliente1.mostrar_informacion())
print(cliente2.mostrar_informacion())
print(cliente3.mostrar_informacion())
print(cliente4.mostrar_informacion())

print("\n PRUEBAS DE VALORES DE ATENCION \n")

valor_atencion_cliente1 = cliente1._tipo_cliente.obtener_valor_atencion(TipoAtencion.LIMPIEZA)
print(f"Valor de atención para cliente 1 (LIMPIEZA): {valor_atencion_cliente1} + precio de cita {cliente1._tipo_cliente.valor_cita} ==> TOTAL: {valor_atencion_cliente1 + cliente1._tipo_cliente.valor_cita}")

valor_atencion_cliente2 = cliente2._tipo_cliente.obtener_valor_atencion(TipoAtencion.CALZAS)
print(f"Valor de atención para cliente 2 (CALZAS): {valor_atencion_cliente2} + precio de cita {cliente2._tipo_cliente.valor_cita} ==> TOTAL: {valor_atencion_cliente2 + cliente2._tipo_cliente.valor_cita}")

valor_atencion_cliente3 = cliente3._tipo_cliente.obtener_valor_atencion(TipoAtencion.EXTRACCION)
print(f"Valor de atención para cliente 3 (EXTRACCION): {valor_atencion_cliente3} + precio de cita {cliente3._tipo_cliente.valor_cita} ==> TOTAL: {valor_atencion_cliente3 + cliente3._tipo_cliente.valor_cita}")

valor_atencion_cliente4 = cliente4._tipo_cliente.obtener_valor_atencion(TipoAtencion.DIAGNOSTICO)
print(f"Valor de atención para cliente 4 (DIAGNOSTICO): {valor_atencion_cliente4} + precio de cita {cliente4._tipo_cliente.valor_cita} ==> TOTAL: {valor_atencion_cliente4 + cliente4._tipo_cliente.valor_cita}")