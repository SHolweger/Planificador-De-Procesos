import random
from procesos import Process

def generate_workload():
    try:
        num_processes = int(input("Ingresa el número de procesos a simular: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return []

    processes = []
    for i in range(num_processes):
        tiempo_llegada = random.randint(0, 10)
        tiempo_ejecucion = random.randint(1, 10)
        prioridad = random.randint(1, 5)
        process = Process(pid=i + 1, tiempo_llegada=tiempo_llegada, tiempo_ejecucion=tiempo_ejecucion, prioridad=prioridad) 
        processes.append(process)

    return processes