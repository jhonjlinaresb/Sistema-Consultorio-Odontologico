from datetime import date
from src.modelos.cliente import Cliente
from src.modelos.tipo_cliente import TipoCliente
from src.modelos.tipo_atencion import TipoAtencion
from src.modelos.prioridad_atencion import PrioridadAtencion
from src.modelos.cita import Cita
from src.modelos.consultorio import Consultorio
from src.excepciones.cantidad_invalida_error import CantidadInvalidaError

cliente1 = Cliente(123456789, "Juan Perez", 5551234, TipoCliente.PARTICULAR)
cliente2 = Cliente(987654321, "Maria Gomez", 5555678, TipoCliente.EPS)
cliente3 = Cliente(456789123, "Carlos Rodriguez", 5559876, TipoCliente.PREPAGADA)
cliente4 = Cliente(111222333, "Ana Martinez", 5554321, TipoCliente.PARTICULAR)

print(cliente1.mostrar_informacion())
print(cliente2.mostrar_informacion())
print(cliente3.mostrar_informacion())
print(cliente4.mostrar_informacion())

print("\n PRUEBAS DE VALORES DE ATENCION CON CANTIDAD, PRIORIDAD Y FECHA \n")

# PRUEBA ERROR: # cita1 = Cita(cliente1, TipoAtencion.LIMPIEZA, cantidad=2, prioridad=PrioridadAtencion.NORMAL, fecha=date(2026, 10, 5)) #Da error porque la cantidad para LIMPIEZA debe ser 1
cita1 = Cita(cliente1, TipoAtencion.LIMPIEZA, cantidad=1, prioridad=PrioridadAtencion.NORMAL, fecha=date(2026, 10, 5))
valor_unitario1 = cliente1._tipo_cliente.obtener_valor_atencion(TipoAtencion.LIMPIEZA)
print(f"Cita Cliente 1 (LIMPIEZA x{cita1.cantidad}) - Prioridad: {cita1.prioridad.value}")
print(f"Valor servicio: {valor_unitario1 * cita1.cantidad} + precio de cita {cliente1._tipo_cliente.valor_cita} ==> TOTAL: {cita1.valor_total_cita()}\n")

cita2 = Cita(cliente2, TipoAtencion.CALZAS, cantidad=3, prioridad=PrioridadAtencion.URGENTE, fecha=date(2026, 10, 6))
valor_unitario2 = cliente2._tipo_cliente.obtener_valor_atencion(TipoAtencion.CALZAS)
print(f"Cita Cliente 2 (CALZAS x{cita2.cantidad}) - Prioridad: {cita2.prioridad.value}")
print(f"Valor servicio: {valor_unitario2 * cita2.cantidad} + precio de cita {cliente2._tipo_cliente.valor_cita} ==> TOTAL: {cita2.valor_total_cita()}\n")

cita3 = Cita(cliente3, TipoAtencion.EXTRACCION, cantidad=2, prioridad=PrioridadAtencion.URGENTE, fecha=date(2026, 10, 7))
valor_unitario3 = cliente3._tipo_cliente.obtener_valor_atencion(TipoAtencion.EXTRACCION)
print(f"Cita Cliente 3 (EXTRACCION x{cita3.cantidad}) - Prioridad: {cita3.prioridad.value}")
print(f"Valor servicio: {valor_unitario3 * cita3.cantidad} + precio de cita {cliente3._tipo_cliente.valor_cita} ==> TOTAL: {cita3.valor_total_cita()}\n")

# cita4 = Cita(cliente4, TipoAtencion.DIAGNOSTICO, cantidad=2, prioridad=PrioridadAtencion.NORMAL, fecha=date(2026, 10, 8)) # PRUEBA ERROR: Da error porque la cantidad para DIAGNOSTICO debe ser 1
cita4 = Cita(cliente4, TipoAtencion.DIAGNOSTICO, cantidad=1, prioridad=PrioridadAtencion.NORMAL, fecha=date(2026, 10, 8))
valor_unitario4 = cliente4._tipo_cliente.obtener_valor_atencion(TipoAtencion.DIAGNOSTICO)
print(f"Cita Cliente 4 (DIAGNOSTICO x{cita4.cantidad}) - Prioridad: {cita4.prioridad.value}")
print(f"Valor servicio: {valor_unitario4 * cita4.cantidad} + precio de cita {cliente4._tipo_cliente.valor_cita} ==> TOTAL: {cita4.valor_total_cita()}\n")

consultorio_doctor_XXX = Consultorio()
consultorio_doctor_XXX.agregar_cita(cita1)
consultorio_doctor_XXX.agregar_cita(cita2)
consultorio_doctor_XXX.agregar_cita(cita3)
consultorio_doctor_XXX.agregar_cita(cita4)

print("\n--- ESTADÍSTICAS DEL CONSULTORIO ---\n")
print(f"Total de clientes atendidos: {consultorio_doctor_XXX.total_clientes()}")
print(f"Ingresos totales recibidos: {consultorio_doctor_XXX.ingresos_totales()}")
print(f"Número de clientes para extracción: {consultorio_doctor_XXX.cantidad_extracciones()}")

print("\n --- ORDENAMIENTO (MÉTODO BURBUJA DESCENDENTE) ---\n")
consultorio_doctor_XXX.ordenar_por_valor_descendente()
for cita in consultorio_doctor_XXX.citas:
    print(f"Cliente: {cita.cliente.nombre}, Valor a pagar: {cita.valor_total_cita()}")

print("\n --- BÚSQUEDA POR CÉDULA ---\n")
cedula_a_buscar = 456789123 #Cédula del cliente3 Carlos Rodriguez
cita_encontrada = consultorio_doctor_XXX.buscar_por_cedula(cedula_a_buscar)

if cita_encontrada:
    print(f"¡Cliente encontrado! Nombre: {cita_encontrada.cliente.nombre}, Tratamiento: {cita_encontrada.tipo_atencion.name}")
else:
    print(f"No se encontró ningún cliente con la cédula {cedula_a_buscar}.")

print("\n --- PRUEBA DE EXCEPCIÓN PERSONALIZADA --- \n")
# PRUEBA 1: 2 Limpiezas
try:
    cita_erronea = Cita(cliente1, TipoAtencion.LIMPIEZA, cantidad=2, prioridad=PrioridadAtencion.NORMAL, fecha=date(2026, 10, 5))
except CantidadInvalidaError as e:
    print(f"ALERTA DEL SISTEMA: {e.mensaje}")

# PRUEBA 2: 2 Diagnósticos
try:
    cita_erronea2 = Cita(cliente2, TipoAtencion.DIAGNOSTICO, cantidad=2, prioridad=PrioridadAtencion.NORMAL, fecha=date(2026, 10, 5))
except CantidadInvalidaError as e:
    print(f"ALERTA DEL SISTEMA: {e.mensaje}")

# PRUEBA 3: Cantidad negativa para calzas
try:  
    cita_erronea3 = Cita(cliente3, TipoAtencion.CALZAS, cantidad=-1, prioridad=PrioridadAtencion.NORMAL, fecha=date(2026, 10, 5))
except CantidadInvalidaError as e:
    print(f"ALERTA DEL SISTEMA: {e.mensaje}")

# PRUEBA 4: Cantidad cero para calzas
try:  
    cita_erronea4 = Cita(cliente4, TipoAtencion.CALZAS, cantidad=0, prioridad=PrioridadAtencion.NORMAL, fecha=date(2026, 10, 5))
except CantidadInvalidaError as e:
    print(f"ALERTA DEL SISTEMA: {e.mensaje}")

#PRUEBA 5: Cantidad negativa para extracción
try:  
    cita_erronea5 = Cita(cliente1, TipoAtencion.EXTRACCION, cantidad=-3, prioridad=PrioridadAtencion.NORMAL, fecha=date(2026, 10, 5))
except CantidadInvalidaError as e:
    print(f"ALERTA DEL SISTEMA: {e.mensaje}")

#PRUEBA 6: Cantidad cero para extracción
try:
    cita_erronea6 = Cita(cliente2, TipoAtencion.EXTRACCION, cantidad=0, prioridad=PrioridadAtencion.NORMAL, fecha=date(2026, 10, 5))
except CantidadInvalidaError as e:
    print(f"ALERTA DEL SISTEMA: {e.mensaje}")

print("\n --- FIN DE PRUEBAS EXCEPCIONES --- \n")