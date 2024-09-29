# src/scheduler.py
from collections import deque
from metrics import calculate_metrics

# Algoritmo FIFO
def fifo_scheduling(processes):
    print("\n--- Ejecución FIFO ---")
    ready_queue = deque(processes)
    time = 0
    completion_times = []

    while ready_queue:
        current_process = ready_queue.popleft()
        print(f"Ejecutando proceso {current_process.pid} con ráfaga de CPU {current_process.tiempo_llegada} (Tiempo actual: {time})")
        time += current_process.tiempo_ejecucion
        current_process.estado = "TERMINATED"
        completion_times.append(time)

    calculate_metrics(processes, completion_times)

# Algoritmo SJF
def sjf_scheduling(processes):
    print("\n--- Ejecución SJF ---")
    processes.sort(key=lambda p: p.tiempo_ejecucion)
    time = 0
    completion_times = []

    for process in processes:
        print(f"Ejecutando proceso {process.pid} con ráfaga de CPU {process.tiempo_ejecucion} (Tiempo actual: {time})")
        time += process.tiempo_ejecucion
        process.estado = "TERMINATED"
        completion_times.append(time)

    calculate_metrics(processes, completion_times)

# Algoritmo Round Robin
def round_robin_scheduling(processes, quantum):
    print("\n--- Ejecución Round Robin ---")
    ready_queue = deque(processes)
    time = 0
    completion_times = []

    while ready_queue:
        current_process = ready_queue.popleft()
        if current_process.tiempo_ejecucion > quantum:
            print(f"Ejecutando proceso {current_process.pid} por {quantum} unidades de tiempo (Tiempo actual: {time})")
            current_process.tiempo_ejecucion -= quantum
            time += quantum
            ready_queue.append(current_process)
        else:
            print(f"Ejecutando proceso {current_process.pid} por {current_process.tiempo_ejecucion} unidades de tiempo (Tiempo actual: {time})")
            time += current_process.tiempo_ejecucion
            current_process.tiempo_ejecucion = 0
            current_process.estado = "TERMINATED"
            completion_times.append(time)

    calculate_metrics(processes, completion_times)

# Algoritmo por Prioridad
def priority_scheduling(processes):
    print("\n--- Ejecución por Prioridad ---")
    processes.sort(key=lambda p: p.prioridad)
    time = 0
    completion_times = []

    for process in processes:
        print(f"Ejecutando proceso {process.pid} con prioridad {process.prioridad} (Tiempo actual: {time})")
        time += process.tiempo_ejecucion
        process.estado = "TERMINATED"
        completion_times.append(time)

    calculate_metrics(processes, completion_times)

def multiprogramacion(planificador, procesos, grado_multiprogramacion):
    cola_espera = []  # Procesos esperando para entrar en memoria
    memoria = []  # Procesos que están en memoria
    
    for proceso in procesos:
        if len(memoria) < grado_multiprogramacion:
            memoria.append(proceso)
            proceso.estado = 'READY'
        else:
            proceso.estado = 'SWAPPED'
            cola_espera.append(proceso)
    
    while memoria or cola_espera:
        if memoria:
            # Seleccionar el proceso siguiente de acuerdo al algoritmo de planificación
            proceso = planificador(memoria)
            if proceso:
                ejecutar_proceso(proceso)
                if proceso.estado == 'TERMINATED':
                    memoria.remove(proceso)
                    
        # Verificar si se puede agregar un proceso de la cola de espera
        if cola_espera and len(memoria) < grado_multiprogramacion:
            proceso_swapped_in = cola_espera.pop(0)
            proceso_swapped_in.estado = 'READY'
            memoria.append(proceso_swapped_in)

# Swapping y manejo de multiprogramación
def swapping(memoria, cola_bloqueados):
    for proceso in memoria:
        if proceso.estado == 'BLOCKED':
            proceso.estado = 'SUSPENDED'
            memoria.remove(proceso)
            cola_bloqueados.append(proceso)

    # Intentar traer procesos suspendidos de vuelta cuando haya espacio
    if cola_bloqueados:
        proceso_swapped_in = cola_bloqueados.pop(0)
        proceso_swapped_in.estado = 'READY'
        memoria.append(proceso_swapped_in)

def multiprogramacion_con_swapping(planificador, procesos, grado_multiprogramacion):
    cola_espera = []
    memoria = []
    cola_bloqueados = []
    
    for proceso in procesos:
        if len(memoria) < grado_multiprogramacion:
            memoria.append(proceso)
            proceso.estado = 'READY'
        else:
            proceso.estado = 'SWAPPED'
            cola_espera.append(proceso)
    
    while memoria or cola_espera:
        # Ejecutar swapping
        swapping(memoria, cola_bloqueados)
        
        if memoria:
            proceso = planificador(memoria)
            if proceso and proceso.estado == 'READY':
                ejecutar_proceso(proceso)
                if proceso.estado == 'TERMINATED':
                    memoria.remove(proceso)
        
        # Verificar si se puede agregar un proceso de la cola de espera
        if cola_espera and len(memoria) < grado_multiprogramacion:
            proceso_swapped_in = cola_espera.pop(0)
            proceso_swapped_in.estado = 'READY'
            memoria.append(proceso_swapped_in)
    
    # Aquí llama a calcular métricas solo una vez después de que todos los procesos han terminado
    completion_times = [p.completion_time for p in procesos if p.estado == 'TERMINATED']
    calculate_metrics(procesos, completion_times)

# Manejo de Entradas/Salidas
def manejar_entradas_salidas(procesos_bloqueados, cola_io):
    for proceso in procesos_bloqueados:
        if proceso.io_bound:
            proceso.estado = 'BLOCKED'
            cola_io.append(proceso)
        else:
            proceso.estado = 'READY'

def planificacion_con_io(planificador, procesos, grado_multiprogramacion):
    cola_espera = []
    memoria = []
    cola_io = []
    
    for proceso in procesos:
        if len(memoria) < grado_multiprogramacion:
            memoria.append(proceso)
            proceso.estado = 'READY'
        else:
            proceso.estado = 'SWAPPED'
            cola_espera.append(proceso)
    
    while memoria or cola_espera or cola_io:
        manejar_entradas_salidas(memoria, cola_io)
        swapping(memoria, cola_io)
        
        if memoria:
            proceso = planificador(memoria)
            if proceso and proceso.estado == 'READY':
                ejecutar_proceso(proceso)
                if proceso.estado == 'TERMINATED':
                    memoria.remove(proceso)

        if cola_espera and len(memoria) < grado_multiprogramacion:
            proceso_swapped_in = cola_espera.pop(0)
            proceso_swapped_in.estado = 'READY'
            memoria.append(proceso_swapped_in)
    
    # Calcular métricas al final
    completion_times = [p.completion_time for p in procesos if p.estado == 'TERMINATED']
    calculate_metrics(procesos, completion_times)
            
def ejecutar_proceso(proceso):
    print(f"Ejecutando el proceso {proceso.pid} con tiempo restante de {proceso.remaining_time}")
    
    # Simulamos que el proceso se ejecuta por 1 unidad de tiempo (esto puede ajustarse)
    proceso.remaining_time -= 1
    
    if proceso.remaining_time <= 0:
        proceso.estado = 'TERMINATED'
        print(f"Proceso {proceso.pid} terminado.")
    else:
        proceso.estado = 'READY'  # El proceso vuelve a estar listo después de ejecutarse