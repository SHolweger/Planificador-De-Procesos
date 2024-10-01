class Recurso:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
        self.asignados = 0

    # Verificar si hay suficientes recursos disponibles
    def puede_asignar(self, cantidad_solicitada):
        return (self.cantidad - self.asignados) >= cantidad_solicitada

    # Asignar recursos a un proceso
    def asignar(self, cantidad):
        if self.puede_asignar(cantidad):
            self.asignados += cantidad
            return True
        return False

    # Liberar recursos después de que un proceso termine
    def liberar(self, cantidad):
        self.asignados -= cantidad