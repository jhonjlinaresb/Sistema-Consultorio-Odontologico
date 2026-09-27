from src.modelos.cliente import Cliente
from src.modelos.tipo_cliente import TipoCliente

cliente1 = Cliente(123456789, "Juan Perez", 5551234, TipoCliente.PARTICULAR)
cliente2 = Cliente(987654321, "Maria Gomez", 5555678, TipoCliente.EPS)
cliente3 = Cliente(456789123, "Carlos Rodriguez", 5559876, TipoCliente.PREPAGADA)

print(cliente1.mostrar_informacion())
print(cliente2.mostrar_informacion())
print(cliente3.mostrar_informacion())