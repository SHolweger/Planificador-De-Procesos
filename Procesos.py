class Process:
    def __init__(self, pid, tiempo_llegada, tiempo_ejecucion, prioridad=0, io_bound=False):
        self.pid = pid  # Identificador del proceso
        self.tiempo_llegada = tiempo_llegada  # Tiempo de llegada
        self.tiempo_ejecucion = tiempo_ejecucion  # Ráfaga de CPU, tiempo de ejecución
        self.tiempo_restante = tiempo_ejecucion  # Tiempo restante para completar el proceso
        self.prioridad = prioridad  # Prioridad
        self.io_bound = io_bound  # Indica si el proceso es I/O bound
        self.start_time = None  # Tiempo de inicio del proceso
        self.completion_time = None  # Tiempo de finalización
        self.estado = "NEW"  # Estado inicial del proceso

    def __str__(self):
        return (f"Proceso {self.pid}: " 
                f"Tiempo de llegada={self.tiempo_llegada}, " 
                f"Tiempo de ejecución={self.tiempo_ejecucion}, "
                f"Prioridad={self.prioridad}, "
                f"Estado={self.estado}")