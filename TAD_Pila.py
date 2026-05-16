from tad_envio import *
from datetime import datetime

# =========================================================
# TAD PILA DE ENVÍOS
# =========================================================

def crearPila():
    # Crea una pila vacía
    pila = []
    return pila

def pilaVacia(pila):
    # Retorna True si la pila está vacía, False si no
    return len(pila) == 0

def apilar(pila, envio):
    # Agrega un envío al tope de la pila
    pila.append(envio)

def desapilar(pila):
    # Quita y retorna el envío del tope de la pila
    return pila.pop()

def tope(pila):
    # Retorna el envío del tope sin sacarlo
    return pila[-1]

def tamanio(pila):
    # Retorna la cantidad de envíos en la pila
    return len(pila)

# =========================================================
# RESPALDO: copia todos los elementos de pila en pilaAux
# =========================================================

def respaldar(pila, pilaAux):
    # Pasa todos los elementos de pila a pilaAux (quedan en orden invertido)
    while not pilaVacia(pila):
        apilar(pilaAux, desapilar(pila))

def restaurar(pilaAux, pila):
    # Restaura los elementos desde pilaAux a pila (vuelven al orden original)
    while not pilaVacia(pilaAux):
        apilar(pila, desapilar(pilaAux))

# =========================================================
# DESPACHO PRIORITARIO
# Desapila y muestra todos los envíos entre fecha1 y fecha2
# Los que NO entran en el rango se conservan en la pila original
# =========================================================

def despacharPorRango(pila, fecha1, fecha2):
    # fecha1 y fecha2 son objetos datetime

    auxiliar = crearPila()

    # Paso los elementos a auxiliar (orden invertido, fondo de pila queda en tope)
    respaldar(pila, auxiliar)

    print("\n========== DESPACHO PRIORITARIO ==========\n")
    hayDespachados = False

    # Recorro desde el fondo de la pila original (tope de auxiliar)
    while not pilaVacia(auxiliar):
        envio = desapilar(auxiliar)
        fecha = datetime.strptime(verFecha(envio), "%d/%m/%y")

        if fecha1 <= fecha <= fecha2:
            # Este envío se despacha
            print("Envío despachado:")
            mostrarEnvio(envio)
            print("-----------------------------")
            hayDespachados = True
        else:
            # Este envío se conserva, lo apilo de vuelta
            apilar(pila, envio)

    if not hayDespachados:
        print("No hay envíos en ese rango de fechas.")

# =========================================================
# ELIMINACIÓN
# Elimina de la pila todos los envíos de un mes dado
# Reconstruye la pila conservando el orden original
# =========================================================

def eliminarPorMes(pila, mes):
    # mes es un entero (1-12)

    auxiliar = crearPila()
    nueva = crearPila()

    # Paso todo a auxiliar (orden invertido)
    respaldar(pila, auxiliar)

    eliminados = 0

    # Recorro desde el fondo de la pila original
    while not pilaVacia(auxiliar):
        envio = desapilar(auxiliar)
        fecha = datetime.strptime(verFecha(envio), "%d/%m/%y")

        if fecha.month != mes:
            # Se conserva
            apilar(nueva, envio)
        else:
            eliminados += 1

    # Reconstruyo la pila original con los que quedaron
    restaurar(nueva, pila)

    print(f"\nSe eliminaron {eliminados} envío(s) del mes {mes}.")

# =========================================================
# MOSTRAR PILA completa (sin modificarla)
# =========================================================

def mostrarPila(pila):
    if pilaVacia(pila):
        print("\nLa pila está vacía.")
        return

    auxiliar = crearPila()

    print("\n========== PILA DE ENVÍOS ==========\n")

    # Desapilo mostrando y guardo en auxiliar
    while not pilaVacia(pila):
        envio = desapilar(pila)
        mostrarEnvio(envio)
        print("-----------------------------")
        apilar(auxiliar, envio)

    # Restauro la pila original
    restaurar(auxiliar, pila)
