import threading
import time
import random

# Recurso compartido: inventario
inventario_modems = 3

# Semáforo para controlar acceso al inventario
mutex = threading.Semaphore(1)


def registrar_pedido(id_pedido):
    global inventario_modems

    print(f"🧾 Pedido {id_pedido} iniciado")

    time.sleep(random.randint(1,3))

    print(f"Pedido {id_pedido} intentando acceder al inventario...")

    mutex.acquire()

    try:
        print(f"Pedido {id_pedido} accedió al inventario")

        if inventario_modems > 0:
            print(f"Pedido {id_pedido} reservando modem...")
            inventario_modems -= 1
            time.sleep(2)
            print(f"Pedido {id_pedido} completado ✅")
        else:
            print(f"Pedido {id_pedido} ❌ no hay modems disponibles")

    finally:
        print(f"Pedido {id_pedido} liberando inventario")
        mutex.release()


def facturacion(id_factura):
    print(f"💳 Facturación procesando pago {id_factura}")
    time.sleep(random.randint(1,3))
    print(f"Pago {id_factura} registrado correctamente")


def soporte_tecnico(id_ticket):
    print(f"🛠️ Soporte técnico atendiendo ticket {id_ticket}")
    time.sleep(random.randint(1,3))
    print(f"Ticket {id_ticket} resuelto")


def main():

    print("\n===== SISTEMA SSSM CON CONCURRENCIA =====\n")

    hilos = []

    # Módulo pedidos
    for i in range(3):
        hilo = threading.Thread(target=registrar_pedido, args=(i+1,))
        hilos.append(hilo)

    # Facturación
    hilo_factura = threading.Thread(target=facturacion, args=(1,))
    hilos.append(hilo_factura)

    # Soporte
    hilo_soporte = threading.Thread(target=soporte_tecnico, args=(1,))
    hilos.append(hilo_soporte)

    # iniciar hilos
    for h in hilos:
        h.start()

    # esperar hilos
    for h in hilos:
        h.join()

    print("\nSistema finalizado")


if __name__ == "__main__":
    main()
