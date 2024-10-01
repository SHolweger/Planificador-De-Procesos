import time
from Graficas import calculate_metrics

def sjf_scheduling(processes, recursos):
    current_time = 0
    processes.sort(key=lambda p: p.tiempo_ejecucion)  # Ordena los procesos por tiempo de ejecución

    for process in processes:
        if recursos.puede_asignar(1):
            recursos.asignar(1)
            process.set_estado("RUNNING")
            process.start_time = current_time
            print(f"\nEjecutando proceso {process.pid}. \nEstado: {process.estado}. \nTiempo actual: {current_time}")
            time.sleep(2)  # Pausa de 2 segundos
            current_time += process.tiempo_ejecucion
            process.completion_time = current_time
            process.set_estado("TERMINATED")
            recursos.liberar(1)
            print(f"\nProceso {process.pid} completado. \nEstado: {process.estado}. \nTiempo actual: {current_time}")
            print("==================================================== \n")
            time.sleep(2)  # Pausa de 2 segundos
        else:
            process.set_estado("BLOCKED")
            print(f"Proceso {process.pid} no puede iniciar, recursos insuficientes.")
            time.sleep(2)  # Pausa de 2 segundos
    
    detect_deadlock(processes)
    calculate_metrics(processes)

def detect_deadlock(processes):
    blocked_processes = [p for p in processes if p.estado == "BLOCKED"]
    if blocked_processes:
        print("Se detectaron procesos bloqueados.")
        time.sleep(2)  # Pausa de 2 segundos
        for p in blocked_processes:
            print(f"Resolviendo interbloqueo para el proceso {p.pid}.")
            p.set_estado("TERMINATED")
            time.sleep(2)  # Pausa de 2 segundos
