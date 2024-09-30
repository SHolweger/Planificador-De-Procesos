import matplotlib.pyplot as plt

def calculate_metrics(processes, completion_times):
    turnaround_times = []
    waiting_times = []
    response_times = []
    tiempos_inicio = []
    tiempos_fin = []

    for i, process in enumerate(processes):
        turnaround_time = completion_times[i] - 0  # Supone que los procesos llegan en t=0
        waiting_time = turnaround_time - process['burst_time']
        response_time = waiting_time  # En muchos casos, el tiempo de respuesta es igual al tiempo de espera
        
        turnaround_times.append(turnaround_time)
        waiting_times.append(waiting_time)
        response_times.append(response_time)
        
        # Aquí asumimos que el tiempo de inicio es el momento en el que comienza el proceso
        tiempos_inicio.append(i if i == 0 else completion_times[i-1])  # Asumimos que el proceso anterior termina y el siguiente empieza inmediatamente
        tiempos_fin.append(completion_times[i])

        print(f"\nProceso {process['pid']}:")
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
    
    # Llamamos a la función para dibujar el diagrama de Gantt
    dibujar_diagrama_gantt([p['pid'] for p in processes], tiempos_inicio, tiempos_fin)

def visualize_metrics(turnaround_times, waiting_times, response_times, processes):
    labels = [f"P{process['pid']}" for process in processes]

    if len(turnaround_times) == len(waiting_times) == len(response_times) == len(labels):
        fig, ax = plt.subplots()
        ax.plot(labels, turnaround_times, label="Tiempo Requerido", marker='o', color='blue', linestyle='-')
        ax.plot(labels, waiting_times, label="Tiempo de Espera", marker='o', color='red', linestyle='--')
        ax.plot(labels, response_times, label="Tiempo de Respuesta", marker='o', color='green', linestyle=':')

        ax.set_xlabel('Procesos')
        ax.set_ylabel('Tiempo')
        ax.set_title('Métricas de Planificación de Procesos')
        ax.legend()

        plt.show()
    else:
        print("Error: Las dimensiones de las métricas no coinciden con las etiquetas de los procesos.")

def dibujar_diagrama_gantt(procesos, tiempos_inicio, tiempos_fin):
    fig, gnt = plt.subplots()

    # Definir límites del gráfico
    gnt.set_xlim(0, max(tiempos_fin) + 1)
    gnt.set_ylim(0, len(procesos) + 1)
    
    gnt.set_xlabel('Tiempo')
    gnt.set_ylabel('Procesos')

    # Títulos de los procesos
    gnt.set_yticks([i+1 for i in range(len(procesos))])
    gnt.set_yticklabels([f'Proceso {p}' for p in procesos])

    # Dibujar los intervalos de tiempo de cada proceso
    for i in range(len(procesos)):
        gnt.broken_barh([(tiempos_inicio[i], tiempos_fin[i] - tiempos_inicio[i])], 
                        (i + 0.5, 0.9), facecolors=('tab:blue'))

    # Título del gráfico
    plt.title(f'Diagrama de Gantt - Procesos')

    # Mostrar el gráfico
    plt.show()
    #plt.hide()
