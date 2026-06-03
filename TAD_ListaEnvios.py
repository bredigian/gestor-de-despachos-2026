from TAD_Envio import *
from datetime import datetime

def crearListaEnvios():
    return []

def listaEnviosVacia(lista):
    return len(lista) == 0

def agregarEnvio(lista, envio):
    lista.append(envio)
    lista.sort(key=lambda envio: datetime.strptime(verFecha(envio), '%d/%m/%Y %H:%M'))

def buscarEnvioPorID(lista, id):
    for envio in lista:
        envioId = verID(envio)
        if envioId.lower() == id.lower():
            return envio
    return None

def eliminarEnvio(lista, envio):
    if envio in lista:
        lista.remove(envio)