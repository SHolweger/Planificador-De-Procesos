from metrics import calculate_metrics

def fifo_scheduling(processes):
    current_time = 0
    completion_times = []
    
    for process in processes:
        current_time += process['burst_time']
        completion_times.append(current_time)
        print(f"Ejecutando proceso {process['pid']} completamente. Tiempo actual: {current_time}")

    calculate_metrics(processes, completion_times)

def sjf_scheduling(processes):
    current_time = 0
    processes.sort(key=lambda x: x['burst_time'])  # Ordenar por tiempo de ráfaga
    completion_times = []
    
    for process in processes:
        current_time += process['burst_time']
        completion_times.append(current_time)
        print(f"Ejecutando proceso {process['pid']} completamente. Tiempo actual: {current_time}")

    calculate_metrics(processes, completion_times)

def round_robin_scheduling(processes, quantum):
    current_time = 0
    remaining_bursts = {process['pid']: process['burst_time'] for process in processes}
    completion_times = {}
    
    while remaining_bursts:
        for process in processes:
            pid = process['pid']
            if pid in remaining_bursts:
                if remaining_bursts[pid] > quantum:
                    current_time += quantum
                    remaining_bursts[pid] -= quantum
                    print(f"Ejecutando proceso {pid} por {quantum} unidades de tiempo. Tiempo actual: {current_time}")
                else:
                    current_time += remaining_bursts[pid]
                    print(f"Ejecutando proceso {pid} por {remaining_bursts[pid]} unidades de tiempo. Tiempo actual: {current_time}")
                    completion_times[pid] = current_time
                    del remaining_bursts[pid]

    completion_times_list = [completion_times[process['pid']] for process in processes]
    calculate_metrics(processes, completion_times_list)

def priority_scheduling(processes):
    current_time = 0
    processes.sort(key=lambda x: x['priority'])  # Ordenar por prioridad
    completion_times = []
    
    for process in processes:
        current_time += process['burst_time']
        completion_times.append(current_time)
        print(f"Ejecutando proceso {process['pid']} completamente. Tiempo actual: {current_time}")

    calculate_metrics(processes, completion_times)

def multiprogramming_swapping(processes, degree):
    current_time = 0
    completion_times = []
    
    for process in processes:
        current_time += process['burst_time']
        completion_times.append(current_time)
        print(f"Ejecutando proceso {process['pid']}. Tiempo actual: {current_time}")

    calculate_metrics(processes, completion_times)

def io_scheduling(processes, degree):
    current_time = 0
    completion_times = []
    
    for process in processes:
        current_time += process['burst_time']
        completion_times.append(current_time)
        print(f"Ejecutando proceso {process['pid']} completamente. Tiempo actual: {current_time}")

    calculate_metrics(processes, completion_times)
