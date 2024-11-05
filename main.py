"""
Sistemas Operativos Laboratorio 1. Trabajo con llamadas al sistema
"""
import random

from src.first_come import fcfs
from src.round_robin import round_robin
from src.shortest_job import sjf

class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time

def main():
    # Genera procesos de prueba
    num_processes = 5
    processes = [Process(i, random.randint(1, 10)) for i in range(num_processes)]

    print("Procesos y sus tiempos de ejecución:")
    for p in processes:
        print(f"PID: {p.pid}, Tiempo de ejecución: {p.burst_time}")

    print("\n--- Algoritmo FCFS ---")
    avg_waiting_fcfs, avg_turnaround_fcfs = fcfs(processes.copy())
    print(f"Tiempo de espera promedio: {avg_waiting_fcfs:.2f}")
    print(f"Tiempo de respuesta promedio: {avg_turnaround_fcfs:.2f}")

    print("\n--- Algoritmo SJF ---")
    avg_waiting_sjf, avg_turnaround_sjf = sjf(processes.copy(), fcfs)
    print(f"Tiempo de espera promedio: {avg_waiting_sjf:.2f}")
    print(f"Tiempo de respuesta promedio: {avg_turnaround_sjf:.2f}")

    print("\n--- Algoritmo Round Robin ---")
    time_quantum = 3
    avg_waiting_rr, avg_turnaround_rr = round_robin(processes.copy(), time_quantum)
    print(f"Tiempo de espera promedio: {avg_waiting_rr:.2f}")
    print(f"Tiempo de respuesta promedio: {avg_turnaround_rr:.2f}")

if __name__ == "__main__":
    main()

