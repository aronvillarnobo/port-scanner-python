# Desarrollado por Aron - Abril 2026

import socket
import time
import threading
from queue import Queue     # Gestión de tareas para multihilo
from datetime import datetime

# Banner visual para la identidad de la herramienta
print("""
    #########################################
    #       ARON'S PORT SCANNER PRO         #
    #    -------------------------------    #
    #      Ethical Hacking Tool v2.0.0      #
    #########################################
""")


def escaneo(objetivo, puerto):
    # AF_INET para IPv4 y SOCK_STREAM para protocolo TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Tiempo máximo de espera para considerar el puerto como cerrado
    s.settimeout(0.5)

    # Intento de conexión: retorna 0 si el puerto está abierto
    resultado = s.connect_ex((objetivo, puerto))

    if resultado == 0:
        try:
            # Banner Grabbing: intentamos obtener info del servicio (versión, nombre)
            banner = s.recv(1024).decode(errors='ignore').strip()
            if not banner:
                banner = "Sin respuesta (Puerto silencioso)"  # El servicio abrió la conexión pero no envió identificación
        except:
            # Si el servicio no responde texto, evitando que se rompa el programa
            banner = "No se pudo obtener el banner"

        s.close()

        return f"[+] Puerto {puerto} abierto | Banner: {banner}"
    s.close()
    return None     # Retornamos None para que el reporte ignore los puertos cerrados

    

# Configuración inicial del escaneo
target = input("Ingrese la direccion IP a escanear: ")

try:
    socket.gethostbyname(target)
except socket.gaierror:
    print("\n[!] Error: Dirección IP o Host inválido.")
    exit()

inicio = time.time()
cola = Queue()  # Cola de puertos pendientes
reporte = []    # Lista para almacenar los puertos conectados

print(f"Escaneando {target}... ")

def threader():     # Worker para procesar la cola
    while True:
        puerto = cola.get()      # Obtiene puerto de la cola
        res = escaneo(target, puerto)
        if res:
            print(res)
            reporte.append(res)
        cola.task_done()     # Marca tarea como finalizada

# Creación del pool de hilos
for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True     # Cierre forzado de hilos al salir
    t.start()

# Carga de puertos en la cola
for p in range(1, 1501):
    cola.put(p)
try:
    cola.join()     # Espera a que termine la cola
except KeyboardInterrupt:
    print("\n[!] Escaneo interrumpido por el usuario. Saliendo...")
    exit()

# Calculo de estadisticas finales
fin = time.time()
tiempo_total = fin - inicio

# Persistencia de datos: guardamos el reporte en un archivo físico
with open("resultado.txt", "w") as f:
    f.write(f"REPORTE DE SEGURIDAD - {target}\n")
    f.write(f"Tiempo de ejecucion: {tiempo_total:.2f} segundos \n")
    f.write("-" * 40 + "\n")
    
    for linea in reporte:
        f.write(linea + "\n")
print(f"\nProceso terminado. Archivo 'resultado.txt' generado.")