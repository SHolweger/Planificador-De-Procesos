from Graficas import calculate_metrics

def priority_scheduling(processes, recursos):
    current_time = 0
    processes.sort(key=lambda x: x.prioridad)
    for process in processes:
        if recursos.asignar(process.tiempo_ejecucion):
            process.set_estado("RUNNING")
            process.start_time = current_time
            print(f"\nEjecutando proceso {process.pid}. \nEstado: {process.estado}. \nTiempo actual: {current_time}")
            current_time += process.tiempo_ejecucion
            process.completion_time = current_time
            process.set_estado("TERMINATED")
            print(f"\nProceso {process.pid} completado. \nEstado: {process.estado}. \nTiempo actual: {current_time}")
            recursos.liberar(process.tiempo_ejecucion)
        else:
            process.set_estado("BLOCKED")
            print(f"Proceso {process.pid} no puede iniciar, recursos insuficientes.")
    
    detect_deadlock(processes)
    calculate_metrics(processes)

def detect_deadlock(processes):
    blocked_processes = [p for p in processes if p.estado == "BLOCKED"]
    if blocked_processes:
        print("Se detectaron procesos bloqueados.")
        for p in blocked_processes:
            print(f"Resolviendo interbloqueo para el proceso {p.pid}.")
            p.set_estado("TERMINATED")
