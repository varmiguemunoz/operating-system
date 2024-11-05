"""
Algoritmo Round Robin ideal para sistemas interactivos que manejan múltiples procesos equitativamente. Asigna tiempo fijo de CPU (quantum) a cada proceso. Si no se completa, se coloca al final de la cola para permitir ejecución de otros procesos.
"""

def round_robin(processes, time_quantum):
    queue = processes[:]
    waiting_time = {p.pid: 0 for p in processes}
    time = 0

    while queue:
        process = queue.pop(0)
        if process.burst_time > time_quantum:
            waiting_time[process.pid] += time + time_quantum
            process.burst_time -= time_quantum
            time += time_quantum
            queue.append(process)  # Reinsertar en la cola
        else:
            time += process.burst_time
            waiting_time[process.pid] += time

    avg_waiting_time = sum(waiting_time.values()) / len(processes)
    avg_turnaround_time = avg_waiting_time + sum(p.burst_time for p in processes) / len(processes)

    return avg_waiting_time, avg_turnaround_time