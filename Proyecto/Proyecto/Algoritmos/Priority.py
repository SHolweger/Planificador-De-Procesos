# src/algorithms/priority.py
def priority_scheduling(ready_queue):
    return min(ready_queue.queue, key=lambda p: p.priority)  # Selecciona el proceso con la prioridad más alta (valor más bajo)
