"""
Algoritmo que ejecuta procesos en orden de llegada a la cola de listos. Implementación fácil pero puede generar alto tiempo de espera debido al efecto "convoy". Requiere ordenar procesos por llegada y ejecutar en secuencia.
"""

def fcfs(processes):
    waiting_time = []
    turnaround_time = []

    waiting_time.append(0)  # El primer proceso no espera
    for i in range(1, len(processes)):
        waiting_time.append(waiting_time[i-1] + processes[i-1].burst_time)

    for i in range(len(processes)):
        turnaround_time.append(waiting_time[i] + processes[i].burst_time)

    avg_waiting_time = sum(waiting_time) / len(processes)
    avg_turnaround_time = sum(turnaround_time) / len(processes)

    return avg_waiting_time, avg_turnaround_time