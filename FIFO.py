from Graficas import calculate_metrics
# proyecto/algoritmos/fifo.py
def fifo_scheduling(processes):
    current_time = 0
    for process in processes:
        current_time += process.tiempo_ejecucion
        process.completion_time = current_time
        print(f"Ejecutando proceso {process.pid} completamente. Tiempo actual: {current_time}")
    calculate_metrics(processes, [process.completion_time for process in processes])
