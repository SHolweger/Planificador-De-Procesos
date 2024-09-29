# src/algorithms/fifo.py
def fifo_scheduling(ready_queue):
    return ready_queue.dequeue()  # Selecciona el primer proceso que llegó
