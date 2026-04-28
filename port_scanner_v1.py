# Desarrollado por Aron - Abril 2026

import socket
import time
from datetime import datetime

# Banner visual para la identidad de la herramienta
print("""
    #########################################
    #       ARON'S PORT SCANNER PRO         #
    #    -------------------------------    #
    #      Ethical Hacking Tool v1.0.0      #
    #########################################
""")

def escaneo(objetivo, puerto):
    # AF_INET para IPv4 y SOCK_STREAM para protocolo TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Tiempo máximo de espera para considerar el puerto como cerrado
    s.settimeout(0.3)

    # Intento de conexión: retorna 0 si el puerto está abierto
    resultado = s.connect_ex((objetivo, puerto))

    if resultado == 0:
        try:
            # Banner Grabbing: intentamos obtener info del servicio (versión, nombre)
            banner = s.recv(1024).decode().strip()
            if not banner:
                banner = "Sin respuesta de banner"
        except:
            # Si el servicio no responde texto, evitando que se rompa el programa
            banner = "No se pudo obtener el banner"

        s.close()

        return f"[+] Puerto {puerto} abierto | Banner: {banner}"
    s.close()
    return None

# Configuración inicial del escaneo
target = input("Ingrese la direccion IP a escanear: ")
inicio = time.time()
reporte = []    # Lista para almacenar los puertos conectados

print(f"Escaneando {target}... ")

try:
    # Bucle principal de escaneo
    for p in range(1, 501):
        res = escaneo(target, p)

        if res:
            print(res)
            reporte.append(res)     # Se guarda el puerto hallado
except KeyboardInterrupt:
    # Permite salir del programa con Ctrl+C
    print("\n[!] Escaneo interrumpido.")

except socket.gaierror:
    # Captura errores de dirección
    print("\n[!] Error: No se pudo resolver el nombre del host o la IP es inválida.")
    exit()

except socket.error:
    # Captura errores generales de conexión con el servidor
    print("\n[!] Error: No se pudo establecer conexión con el servidor.")
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