from Graficas import calculate_metrics
# proyecto/algoritmos/fifo.py
def fifo_scheduling(processes):
    current_time = 0
    for process in processes:
        print(f"Proceso {process.pid}: Estado: NEW")
        process.estado = "RUNNING"
        process.start_time = current_time
        print(f"Ejecutando proceso {process.pid}. Estado: {process.estado}. Tiempo actual: {current_time}")
        current_time += process.tiempo_ejecucion
        process.completion_time = current_time
        process.estado = "TERMINATED"
        print(f"Proceso {process.pid} completado. Estado: {process.estado}. Tiempo actual: {current_time}")
    calculate_metrics(processes, [process.completion_time for process in processes])
