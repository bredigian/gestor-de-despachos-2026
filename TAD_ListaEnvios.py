from TAD_Envio import *
from datetime import datetime

def crearListaEnvios():
    return []

def tamanioLista(lista):
    return len(lista)

def listaEnviosVacia(lista):
    return tamanioLista(lista) == 0

def agregarEnvio(lista, envio):
    lista.append(envio)
    lista.sort(key=lambda envio: datetime.strptime(verFecha(envio), '%d/%m/%Y %H:%M'))

def eliminarEnvio(lista, envio):
    lista.remove(envio)

def recuperarEnvio(lista, i):
    return lista[i]