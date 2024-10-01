# Función de planificación FIFO con pausas entre procesos
import time
from Graficas import calculate_metrics
def fifo_scheduling(processes, recursos):
    current_time = 0
    for process in processes:
        if recursos.asignar(process.recursos_necesarios):  # Se usan los recursos necesarios para ese proceso
            recursos.liberar(process.recursos_necesarios)  # Al finalizar, se liberan los mismos recursos
            process.set_estado("RUNNING")
            process.start_time = current_time
            print(f"\nEjecutando proceso {process.pid}. \nEstado: {process.estado}. \nTiempo actual: {current_time}")
            
            time.sleep(2)  # Pausa de 2 segundos para simular ejecución
            current_time += process.tiempo_ejecucion
            
            process.completion_time = current_time
            process.set_estado("TERMINATED")
            recursos.liberar(1)
            print(f"\nProceso {process.pid} completado. \nEstado: {process.estado}. \nTiempo actual: {current_time}")
            print("==================================================== \n")
        else:
            process.set_estado("BLOCKED")
            print(f"Proceso {process.pid} no puede iniciar, recursos insuficientes.")
    
    detect_deadlock(processes)
    calculate_metrics(processes)

# Función que detecta si hay interbloqueo en los procesos
def detect_deadlock(processes):
    blocked_processes = [p for p in processes if p.estado == "BLOCKED"]
    if blocked_processes:
        print("Se detectaron procesos bloqueados.")
        for p in blocked_processes:
            print(f"Resolviendo interbloqueo para el proceso {p.pid}.")
            p.set_estado("TERMINATED")