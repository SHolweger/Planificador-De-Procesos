from Planificador import *
from metrics import calculate_metrics

def run_simulation():
    # Pedir número de procesos
    n = int(input("Ingresa el número de procesos a simular: "))
    
    processes = []
    for i in range(n):
        burst_time = int(input(f"Ingresa el tiempo de ráfaga para el proceso {i+1}: "))
        priority = int(input(f"Ingresa la prioridad para el proceso {i+1}: "))
        processes.append({'pid': i+1, 'burst_time': burst_time, 'priority': priority})

    # Selección de algoritmo
    print("Selecciona un algoritmo de planificación:")
    print("1. FIFO")
    print("2. SJF")
    print("3. Round Robin")
    print("4. Prioridad")
    print("5. Multiprogramación con Swapping")
    print("6. Planificación de E/S")
    
    choice = int(input("Ingresa el número de tu elección: "))

    if choice == 1:
        print("\n--- Ejecución FIFO ---")
        fifo_scheduling(processes)
    elif choice == 2:
        print("\n--- Ejecución SJF ---")
        sjf_scheduling(processes)
    elif choice == 3:
        quantum = int(input("Ingresa el cuanto de tiempo para Round Robin: "))
        print("\n--- Ejecución Round Robin ---")
        round_robin_scheduling(processes, quantum)
    elif choice == 4:
        print("\n--- Ejecución Prioridad ---")
        priority_scheduling(processes)
    elif choice == 5:
        degree = int(input("Ingresa el grado de multiprogramación: "))
        print("\n--- Ejecución Multiprogramación con Swapping ---")
        multiprogramming_swapping(processes, degree)
    elif choice == 6:
        degree = int(input("Ingresa el grado de multiprogramación: "))
        print("\n--- Ejecución Planificación de E/S ---")
        io_scheduling(processes, degree)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    run_simulation()
