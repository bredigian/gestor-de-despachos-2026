from TAD_Envio import *

# =========================================================
# TAD PILA
# =========================================================
    
def crearPila():
    # Crea una pila vacía
    pila=[]
    return pila


def pilaVacia(pila):
    # Retorna True si la pila está vacía, False si no
    return tamanio(pila)==0


def apilar(pila,elemento):
    # Agrega un envío al tope de la pila
    pila.append(elemento)


def desapilar(pila):
    # Quita y retorna el envío del tope de la pila
    return pila.pop()


def tamanio(pila):
    # Retorna la cantidad de envíos en la pila
    return len(pila)

def copiarPila(pila, pila2):
    # Copia los datos de la pila 2 a la pila
    auxiliar = crearPila()

    while not pilaVacia(pila2):
        envio = desapilar(pila2)
        apilar(auxiliar,envio)
    while not pilaVacia(auxiliar):
        envio = desapilar(auxiliar)
        apilar(pila,envio)