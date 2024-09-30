from Graficas import calculate_metrics
from FIFO import fifo_scheduling
from Priority import priority_scheduling
from RR import round_robin_scheduling
from SJF import sjf_scheduling
from Procesos import Process

def run_simulation():
    print("\n============= Planificador de Procesos ============= ")

    n = int(input("¿Cuántos procesos desea simular?\n"))
    
    processes = []
    for i in range(n):
        burst_time = int(input(f"Ingresa el tiempo de ráfaga para el proceso {i+1}: "))
        priority = int(input(f"Ingresa la prioridad para el proceso {i+1}: "))
        process = Process(pid=i+1, tiempo_llegada=0, tiempo_ejecucion=burst_time, prioridad=priority)
        processes.append(process)

    print("================= Elige una opción ================= ")
    print("1. FIFO")
    print("2. SJF")
    print("3. Round Robin")
    print("4. Prioridad")
    print("==================================================== \n")

    choice = int(input("Ingresa el número de tu elección: "))

    if choice == 1:
        print("\n--- Ejecución FIFO ---")
        fifo_scheduling(processes)
        print("\n----------------------")
    elif choice == 2:
        print("\n--- Ejecución SJF ---")
        sjf_scheduling(processes)
        print("\n----------------------")
    elif choice == 3:
        quantum = int(input("Ingresa valor del Quantum: "))
        print("\n--- Ejecución Round Robin ---")
        round_robin_scheduling(processes, quantum)
        print("\n----------------------")
    elif choice == 4:
        print("\n--- Ejecución Prioridad ---")
        priority_scheduling(processes)
        print("\n----------------------")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    run_simulation()