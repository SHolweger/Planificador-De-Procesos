# src/Simulacion.py
from workload import generate_workload
from Planificador import fifo_scheduling, sjf_scheduling, round_robin_scheduling, priority_scheduling

def run_simulation():
    processes = generate_workload()
    
    print("Selecciona un algoritmo de planificación:")
    print("1. FIFO")
    print("2. SJF")
    print("3. Round Robin")
    print("4. Prioridad")
    choice = int(input("Ingresa el número de tu elección: "))

    if choice == 1:
        fifo_scheduling(processes)
    elif choice == 2:
        sjf_scheduling(processes)
    elif choice == 3:
        quantum = int(input("Ingresa el cuanto de tiempo para Round Robin: "))
        round_robin_scheduling(processes, quantum)
    elif choice == 4:
        priority_scheduling(processes)
    else:
        print("Elección no válida")

if __name__ == "__main__":
    run_simulation()
