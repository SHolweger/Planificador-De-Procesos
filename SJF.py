from Graficas import calculate_metrics

def sjf_scheduling(processes):
    current_time = 0
    processes.sort(key=lambda x: x.tiempo_ejecucion)  # Ordenar por tiempo de ráfaga
    for process in processes:
        process.estado = "RUNNING"
        print(f"Ejecutando proceso {process.pid}. Estado: {process.estado}. Tiempo actual: {current_time}")
        current_time += process.tiempo_ejecucion
        process.completion_time = current_time
        process.estado = "TERMINATED"
        print(f"Proceso {process.pid} completado. Estado: {process.estado}. Tiempo actual: {current_time}")
    
    calculate_metrics(processes, [process.completion_time for process in processes])
