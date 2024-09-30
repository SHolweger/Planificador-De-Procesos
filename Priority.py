# proyecto/algoritmos/priority.py
from Graficas import calculate_metrics

def priority_scheduling(processes):
    current_time = 0
    processes.sort(key=lambda x: x.prioridad)  # Ordenar por prioridad
    for process in processes:
        current_time += process.tiempo_ejecucion
        process.completion_time = current_time
        print(f"Ejecutando proceso {process.pid} completamente. Tiempo actual: {current_time}")
    calculate_metrics(processes, [process.completion_time for process in processes])
