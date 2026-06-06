from TAD_ListaEnvios import recuperarEnvio, tamanioLista
from TAD_Envio import verID

def buscarEnvioPorID(lista, id):
    for i in range(tamanioLista(lista)):
        envio = recuperarEnvio(lista, i)
        envioId = verID(envio)
        
        if envioId.lower() == id.lower():
            return envio
        
    return None