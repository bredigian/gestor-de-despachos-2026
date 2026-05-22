from TAD_Envio import *

# =========================================================
# TAD PILA DE ENVÍOS
# =========================================================

def crearPila():
    # Crea una pila vacía
    pila = []
    return pila

def apilar(pila, envio):
    # Agrega un envío al tope de la pila
    pila.append(envio)

def desapilar(pila, pilaAux):
    # Quita y retorna el envío del tope de la pila
    envioADesapilar = pila.pop()
    apilar(pilaAux, envioADesapilar)
    
    return envioADesapilar

def tope(pila):
    # Retorna el envío del tope sin sacarlo
    return pila[-1]

def tamanio(pila):
    # Retorna la cantidad de envíos en la pila
    return len(pila)

def pilaVacia(pila):
    # Retorna True si la pila está vacía, False si no
    return tamanio(pila) == 0

# =========================================================
# respaldar(): copia todos los elementos de pila en pilaAux
# restaurar(): copia todos los elementos de pilaAux de vuelta a pila
# =========================================================

def respaldar(pila, pilaAux):
    # Pasa todos los envios de pila a pilaAux (quedan en orden invertido)
    while not pilaVacia(pila):
        desapilar(pila, pilaAux)

def restaurar(pilaAux, pila):
    # Restaura los envios desde pilaAux a pila (vuelven al orden original)
    while not pilaVacia(pilaAux):
        apilar(pila, desapilar(pilaAux, pila))

# =========================================================
# mostrarPila(): muestra los envíos en la pila sin modificar su orden
# =========================================================

def mostrarPila(pila):
    if pilaVacia(pila):
        print("\nLa pila está vacía.")
        return

    auxiliar = crearPila()

    # Desapilo mostrando y guardo en auxiliar
    while not pilaVacia(pila):
        envio = desapilar(pila, auxiliar)
        mostrarEnvio(envio)
        apilar(auxiliar, envio)

    # Restauro la pila original
    restaurar(auxiliar, pila)
