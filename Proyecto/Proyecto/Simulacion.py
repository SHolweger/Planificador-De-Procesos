from workload import generate_workload
from Planificador import (fifo_scheduling, sjf_scheduling, round_robin_scheduling, priority_scheduling,multiprogramacion,multiprogramacion_con_swapping,planificacion_con_io)

def run_simulation():
    processes = generate_workload()

    print("Selecciona un algoritmo de planificación:")
    print("1. FIFO")
    print("2. SJF")
    print("3. Round Robin")
    print("4. Prioridad")
    print("5. Multiprogramación con Swapping")
    print("6. Planificación de E/S")
    
    try:
        choice = int(input("Ingresa el número de tu elección: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return

    if choice == 1:
        fifo_scheduling(processes)
    elif choice == 2:
        sjf_scheduling(processes)
    elif choice == 3:
        try:
            quantum = int(input("Ingresa el cuanto de tiempo para Round Robin: "))
            round_robin_scheduling(processes, quantum)
        except ValueError:
            print("Por favor, ingresa un número válido para el cuanto.")
    elif choice == 4:
        priority_scheduling(processes)
    elif choice == 5:
        try:
            grado_multiprogramacion = int(input("Ingresa el grado de multiprogramación: "))
            multiprogramacion(fifo_scheduling, processes, grado_multiprogramacion)
              # Usando FIFO como planificador, puedes cambiarlo según tu necesidad
        except ValueError:
            print("Por favor, ingresa un número válido para el grado de multiprogramación.")
    elif choice == 6:
        try:
            grado_multiprogramacion = int(input("Ingresa el grado de multiprogramación: "))
            multiprogramacion_con_swapping(fifo_scheduling, processes, grado_multiprogramacion)
            planificacion_con_io(fifo_scheduling, processes, grado_multiprogramacion)  # Usando FIFO como planificador
        except ValueError:
            print("Por favor, ingresa un número válido para el grado de multiprogramación.")
    else:
        print("Elección no válida")

if __name__ == "__main__":
    run_simulation()
