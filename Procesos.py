# Clase para gestionar el estado de un proceso
class Process:
    def __init__(self, pid, tiempo_llegada, tiempo_ejecucion, prioridad=0):
        self.pid = pid
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_ejecucion = tiempo_ejecucion
        self.tiempo_restante = tiempo_ejecucion
        self.prioridad = prioridad
        self.start_time = None
        self.completion_time = None
        self.estado = "NEW"  # Estado inicial

    # Función para cambiar el estado de un proceso
    def set_estado(self, nuevo_estado):
        print(f"Proceso {self.pid}: \nEstado: {self.estado} -> {nuevo_estado}.")
        self.estado = nuevo_estado
        
    def __str__(self):
        return (f"Proceso {self.pid}: "
                f"Tiempo de llegada ={self.tiempo_llegada}, "
                f"Tiempo de ejecución ={self.tiempo_ejecucion}, "
                f"Prioridad ={self.prioridad}, "
                f"Estado ={self.estado}")