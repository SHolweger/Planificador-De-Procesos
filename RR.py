from Graficas import calculate_metrics

def round_robin_scheduling(processes, quantum):
    current_time = 0
    remaining_bursts = {process.pid: process.tiempo_ejecucion for process in processes}
    
    while remaining_bursts:
        for process in processes:
            pid = process.pid
            if pid in remaining_bursts:
                process.estado = "RUNNING"
                print(f"Ejecutando proceso {pid}. Estado: {process.estado}. Tiempo actual: {current_time}")
                
                if remaining_bursts[pid] > quantum:
                    current_time += quantum
                    remaining_bursts[pid] -= quantum
                else:
                    current_time += remaining_bursts[pid]
                    process.completion_time = current_time
                    del remaining_bursts[pid]
                    process.estado = "TERMINATED"
                    print(f"Proceso {pid} completado. Estado: {process.estado}. Tiempo actual: {current_time}")

    calculate_metrics(processes, [process.completion_time for process in processes])
