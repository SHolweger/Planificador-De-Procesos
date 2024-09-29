import matplotlib.pyplot as plt

def calculate_metrics(processes, completion_times):
    turnaround_times = []
    waiting_times = []
    response_times = []

    for i, process in enumerate(processes):
        # Calcular tiempos
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

    # Calcular promedios
    avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)
    avg_waiting_time = sum(waiting_times) / len(waiting_times)
    avg_response_time = sum(response_times) / len(response_times)

    print("\n--- Métricas Promedio ---")
    print(f"Promedio de Tiempo Requerido: {avg_turnaround_time}")
    print(f"Promedio de Tiempo de espera: {avg_waiting_time}")
    print(f"Promedio de Tiempo de respuesta: {avg_response_time}")

    # Visualización de resultados
    visualize_metrics(turnaround_times, waiting_times, response_times)
    plot_gantt_chart(processes)

def visualize_metrics(turnaround_times, waiting_times, response_times):
    labels = [f"P{i+1}" for i in range(len(turnaround_times))]

    fig, ax = plt.subplots()
    
    ax.plot(labels, turnaround_times, label="Tiempo Requerido", marker='o', color='blue', linestyle='-')
    ax.plot(labels, waiting_times, label="Tiempo de espera", marker='o', color='orange', linestyle='--')
    ax.plot(labels, response_times, label="Tiempo de respuesta", marker='o', color='green', linestyle=':')

    ax.set_xlabel('Procesos', fontsize=12)
    ax.set_ylabel('Tiempo (unidades)', fontsize=12)
    ax.set_title('Métricas por Proceso', fontsize=14)
    ax.legend()
    ax.grid(True)

    plt.show()
    plt.close()

def plot_gantt_chart(processes):
    fig, ax = plt.subplots()
    start_time = 0
    
    for process in processes:
        ax.barh(process.pid, process.tiempo_ejecucion, left=start_time, color='lightblue')
        ax.text(start_time + process.tiempo_ejecucion / 2, process.pid, f'{process.pid}', 
                va='center', ha='center', color='black')  # Agregar etiqueta en el medio de la barra
        start_time += process.tiempo_ejecucion
        
    ax.set_xlabel('Tiempo (unidades)', fontsize=12)
    ax.set_ylabel('Proceso', fontsize=12)
    ax.set_title('Gráfico de Gantt', fontsize=14)
    plt.grid(axis='x')
    plt.show()
    plt.close()
