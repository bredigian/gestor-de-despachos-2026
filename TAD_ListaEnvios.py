from TAD_Envio import *

def crearListaEnvios():
    return []

def listaEnviosVacia(lista):
    return len(lista) == 0

def agregarEnvio(lista, envio):
    lista.append(envio)

def buscarEnvioPorID(lista, id):
    for envio in lista:
        envioId = verID(envio)
        if envioId == id:
            return envio
    return None

def eliminarEnvio(lista, envio):
    if envio in lista:
        lista.remove(envio)