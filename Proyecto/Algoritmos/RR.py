# src/algorithms/round_robin.py
def round_robin_scheduling(ready_queue, quantum):
    process = ready_queue.dequeue()
    if process.remaining_time > quantum:
        process.remaining_time -= quantum
        ready_queue.enqueue(process)  # Volver a encolar el proceso si no ha terminado
    else:
        process.remaining_time = 0  # El proceso ha terminado
    return process
