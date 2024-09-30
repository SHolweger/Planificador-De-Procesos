import tkinter as tk
from tkinter import messagebox, simpledialog
from Planificador import (
    fifo_scheduling, 
    sjf_scheduling, 
    round_robin_scheduling, 
    multiprogramacion, 
    multiprogramacion_con_swapping, 
    planificacion_con_io,
    priority_scheduling
)

class ProcessSchedulerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Simulador de Planificación de Procesos")

        self.label = tk.Label(master, text="Selecciona un algoritmo de planificación:")
        self.label.pack()

        self.algorithm_var = tk.StringVar(value="FIFO")
        self.algorithms = ["FIFO", "SJF", "Round Robin", "Prioridad", "Multiprogramación", "Swapping"]
        self.algorithm_menu = tk.OptionMenu(master, self.algorithm_var, *self.algorithms)
        self.algorithm_menu.pack()

        self.run_button = tk.Button(master, text="Ejecutar", command=self.run_simulation)
        self.run_button.pack()

        self.results_text = tk.Text(master, height=20, width=70)
        self.results_text.pack()

    def run_simulation(self):
        selected_algorithm = self.algorithm_var.get()
        processes = self.generate_workload()  # Implementar esta función según tu lógica de procesos
        results = ""

        if selected_algorithm == "FIFO":
            results = fifo_scheduling(processes)
        elif selected_algorithm == "SJF":
            results = sjf_scheduling(processes)
        elif selected_algorithm == "Round Robin":
            quantum = simpledialog.askinteger("Entrada", "Ingresa el quantum para Round Robin:")
            results = round_robin_scheduling(processes, quantum)
        elif selected_algorithm == "Prioridad":
            results = priority_scheduling(processes)
        elif selected_algorithm == "Multiprogramación":
            results = multiprogramacion(processes)
        elif selected_algorithm == "Swapping":
            results = multiprogramacion_con_swapping(processes)

        self.show_results(results)

    def show_results(self, results):
        self.results_text.delete(1.0, tk.END)  # Limpia el texto anterior
        self.results_text.insert(tk.END, results)  # Inserta los nuevos resultados

    def generate_workload(self):
        # Aquí generas la lista de procesos. Este es un ejemplo simple.
        return [
            Process(pid="P1", tiempo_llegada=0, tiempo_ejecucion=4),
            Process(pid="P2", tiempo_llegada=1, tiempo_ejecucion=2),
            Process(pid="P3", tiempo_llegada=2, tiempo_ejecucion=1),
            # Añade más procesos según tu lógica
        ]

class Process:
    def __init__(self, pid, tiempo_llegada, tiempo_ejecucion):
        self.pid = pid
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_ejecucion = tiempo_ejecucion
        self.estado = "NEW"

if __name__ == "__main__":
    root = tk.Tk()
    app = ProcessSchedulerGUI(root)
    root.mainloop()
