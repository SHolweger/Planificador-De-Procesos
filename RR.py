from Graficas import calculate_metrics

def round_robin_scheduling(processes, quantum, recursos):
    current_time = 0
    remaining_bursts = {process.pid: process.tiempo_ejecucion for process in processes}
    
    while remaining_bursts:
        for process in processes:
            pid = process.pid
            if pid in remaining_bursts:
                if recursos.asignar(min(quantum, remaining_bursts[pid])):
                    process.set_estado("RUNNING")
                    process.start_time = current_time
                    print(f"\nEjecutando proceso {process.pid}. \nEstado: {process.estado}. \nTiempo actual: {current_time}")
                    
                    if remaining_bursts[pid] > quantum:
                        current_time += quantum
                        remaining_bursts[pid] -= quantum
                    else:
                        current_time += remaining_bursts[pid]
                        process.completion_time = current_time
                        del remaining_bursts[pid]
                        process.set_estado("TERMINATED")
                        print(f"\nProceso {pid} completado. \nEstado: {process.estado}. \nTiempo actual: {current_time}")
                    recursos.liberar(min(quantum, remaining_bursts.get(pid, 0)))
                else:
                    process.set_estado("BLOCKED")
                    print(f"Proceso {pid} no puede iniciar, recursos insuficientes.")
    
    detect_deadlock(processes)
    calculate_metrics(processes)

def detect_deadlock(processes):
    blocked_processes = [p for p in processes if p.estado == "BLOCKED"]
    if blocked_processes:
        print("Se detectaron procesos bloqueados.")
        for p in blocked_processes:
            print(f"Resolviendo interbloqueo para el proceso {p.pid}.")
            p.set_estado("TERMINATED")
