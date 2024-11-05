"""
El algoritmo SJF busca reducir el tiempo de espera priorizando procesos cortos, pero su desafío es que el tiempo de ejecución no siempre es conocido. Consiste en ordenar y ejecutar procesos por su duración.
"""

def sjf(processes, fcfs):
  processes.sort(key=lambda x: x.burst_time)
  return fcfs(processes)