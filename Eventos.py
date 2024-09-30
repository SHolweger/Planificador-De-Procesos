# proyecto/eventos.py
class Event:
    def __init__(self, tipo_evento, event_time, proceso):
        self.tipo_evento = tipo_evento  # Ej: 'ARRIVAL', 'FINISH_BURST', 'TIME_SLICE'
        self.event_time = event_time  # El tiempo en el que ocurre el evento
        self.proceso = proceso  # El proceso asociado con el evento

    def __str__(self):
        return f"Evento {self.tipo_evento} en {self.event_time} para el proceso {self.proceso.pid}"
