import matplotlib.pyplot as plt

def calculate_metrics(processes, completion_times):
    turnaround_times = []
    waiting_times = []
    response_times = []

    for i, process in enumerate(processes):
        turnaround_time = completion_times[i] - process.tiempo_llegada
        waiting_time = turnaround_time - process.tiempo_ejecucion
        response_time = completion_times[i] - process.tiempo_ejecucion - process.tiempo_llegada

        turnaround_times.append(turnaround_time)
        waiting_times.append(waiting_time)
        response_times.append(response_time)

        print(f"\nProceso {process.pid}:")
        print(f"Tiempo de Tiempo Requerido: {turnaround_time}")
        print(f"Tiempo de Espera: {waiting_time}")
        print(f"Tiempo de Respuesta: {response_time}")

    # Promedios
    avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)
    avg_waiting_time = sum(waiting_times) / len(waiting_times)
    avg_response_time = sum(response_times) / len(response_times)

    print("\n--- Métricas Promedio ---")
    print(f"Promedio de Tiempo Requerido: {avg_turnaround_time}")
    print(f"Promedio de Tiempo de espera: {avg_waiting_time}")
    print(f"Promedio de Tiempo de respuesta: {avg_response_time}")

    # Visualización de resultados
    visualize_metrics(turnaround_times, waiting_times, response_times)

# Función para graficar las métricas
def visualize_metrics(turnaround_times, waiting_times, response_times):
    labels = [f"P{i+1}" for i in range(len(turnaround_times))]

    fig, ax = plt.subplots()
    
    ax.plot(labels, turnaround_times, label="Tiempo Requerido", marker='o')
    ax.plot(labels, waiting_times, label="Tiempo de espera", marker='o')
    ax.plot(labels, response_times, label="Tiempo de respuesta", marker='o')

    ax.set_xlabel('Procesos')
    ax.set_ylabel('Tiempo (unidades)')
    ax.set_title('Métricas por Proceso')
    ax.legend()

    plt.show()
