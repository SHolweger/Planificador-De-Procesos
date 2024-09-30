import matplotlib.pyplot as plt

def calculate_metrics(processes, completion_times):
    turnaround_times = []
    waiting_times = []
    response_times = []

    for i, process in enumerate(processes):
        turnaround_time = completion_times[i] - process.tiempo_llegada
        waiting_time = turnaround_time - process.tiempo_ejecucion
        response_time = waiting_time
        
        turnaround_times.append(turnaround_time)
        waiting_times.append(waiting_time)
        response_times.append(response_time)

        print(f"\nProceso {process.pid}:")
        print(f"Tiempo Requerido (Turnaround Time): {turnaround_time}")
        print(f"Tiempo de Espera (Waiting Time): {waiting_time}")
        print(f"Tiempo de Respuesta (Response Time): {response_time}")

    avg_turnaround = sum(turnaround_times) / len(turnaround_times)
    avg_waiting = sum(waiting_times) / len(waiting_times)
    avg_response = sum(response_times) / len(response_times)
    
    print("\n--- Métricas Promedio ---")
    print(f"Promedio de Tiempo Requerido (Turnaround Time): {avg_turnaround}")
    print(f"Promedio de Tiempo de Espera (Waiting Time): {avg_waiting}")
    print(f"Promedio de Tiempo de Respuesta (Response Time): {avg_response}")

    visualize_metrics(turnaround_times, waiting_times, response_times, processes)

def visualize_metrics(turnaround_times, waiting_times, response_times, processes):
    labels = [f"P{process.pid}" for process in processes]
    fig, ax = plt.subplots()
    ax.plot(labels, turnaround_times, label="Tiempo Requerido", marker='o', color='blue', linestyle='-')
    ax.plot(labels, waiting_times, label="Tiempo de Espera", marker='o', color='red', linestyle='--')
    ax.plot(labels, response_times, label="Tiempo de Respuesta", marker='o', color='green', linestyle=':')

    ax.set_xlabel('Procesos')
    ax.set_ylabel('Tiempo')
    ax.set_title('Métricas de Planificación de Procesos')
    ax.legend()
    plt.show()
