from src.modelos.cliente import Cliente

cliente1 = Cliente(123456789, "Juan Perez", 5551234)
cliente2 = Cliente(987654321, "Maria Gomez", 5555678)
print(cliente1.mostrar_informacion())
print(cliente2.mostrar_informacion())