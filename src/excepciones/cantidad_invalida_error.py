class CantidadInvalidaError(Exception):
    def __init__(self, mensaje = "La cantidad ingresada no es válida para este tratamiento."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)