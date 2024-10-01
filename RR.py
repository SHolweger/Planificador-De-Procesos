import time
from Graficas import calculate_metrics

def round_robin_scheduling(processes, quantum, recursos):
    current_time = 0
    queue = processes[:]  # Cola de procesos

    while queue:
        for process in queue:
            if recursos.puede_asignar(1):
                recursos.asignar(1)
                if process.tiempo_restante == process.tiempo_ejecucion:
                    process.set_estado("RUNNING")
                    process.start_time = current_time

                exec_time = min(quantum, process.tiempo_restante)
                print(f"\nEjecutando proceso {process.pid}. \nEstado: {process.estado}. \nTiempo actual: {current_time}")
                time.sleep(2)  # Pausa de 2 segundos
                current_time += exec_time
                process.tiempo_restante -= exec_time
                
                if process.tiempo_restante == 0:
                    process.completion_time = current_time
                    process.set_estado("TERMINATED")
                    recursos.liberar(1)
                    print(f"\nProceso {process.pid} completado. \nEstado: {process.estado}. \nTiempo actual: {current_time}")
                    print("==================================================== \n")
                    time.sleep(2)  # Pausa de 2 segundos
                    queue.remove(process)
                else:
                    print(f"Proceso {process.pid} no ha terminado. \nEstado: {process.estado}. \nTiempo restante: {process.tiempo_restante}")
                    time.sleep(2)  # Pausa de 2 segundos
                    recursos.liberar(1)
            else:
                process.set_estado("BLOCKED")
                print(f"Proceso {process.pid} no puede continuar, recursos insuficientes.")
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
