# src/algorithms/sjf.py
def sjf_scheduling(ready_queue):
    return min(ready_queue.queue, key=lambda p: p.tiempo_ejecucion)  # Selecciona el proceso con la ráfaga de CPU más corta