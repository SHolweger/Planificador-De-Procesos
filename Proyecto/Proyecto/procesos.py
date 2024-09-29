# src/process.py
class Process:
    def __init__(self, pid, tiempo_llegada, tiempo_ejecucion, prioridad=0, io_bound=False):
        self.pid = pid  # Identificador del proceso
        self.tiempo_llegada = tiempo_llegada  # Tiempo de llegada
        self.tiempo_ejecucion = tiempo_ejecucion  # Ráfaga de CPU, tiempo de ejecución
        self.prioridad = prioridad  # Prioridad
        self.tiempo_restante = tiempo_ejecucion  # Tiempo restante para completar el proceso
        self.estado = "NEW"  # Estado inicial del proceso
        self.time_in_memory = 0  # Tiempo que ha pasado en la memoria
        self.io_bound = io_bound  # Indica si el proceso es I/O bound

    def __str__(self):
        return (f"Proceso {self.pid}: " f"Tiempo de llegada={self.tiempo_llegada}, " f"Tiempo de ejecución={self.tiempo_ejecucion}, "f"Prioridad={self.prioridad}, "f"Estado={self.estado}")