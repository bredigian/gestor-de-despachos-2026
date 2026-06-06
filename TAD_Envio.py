# TAD Envio
# envio = [trackingID, destinatario, categoria, fecha]
#           [0]          [1]           [2]        [3]

def crearEnvio():
    #Crea un envio vacio
    return [None, None, None, None]    

def cargarEnvio(envio, id, destinatario, categoria, fecha):
    #Carga los datos de un envio
    envio[0] = id.strip().lower()
    envio[1] = destinatario.strip().title()
    envio[2] = categoria
    envio[3] = fecha

def verID(envio):
    #Retorna el tracking ID
    return envio[0]

def verDestinatario(envio):
    #Retorna el destinatario
    return envio[1]

def verCategoria(envio):
    #Retorna la categoria
    return envio[2]

def verFecha(envio):
    #Retorna la fecha
    return envio[3]

def modiDestinatario(envio, d):
    #Modifica el destinatario
    envio[1] = d

def modiCategoria(envio, c):
    #Modifica la categoria
    envio[2] = c

def modiFecha(envio, f):
    #Modifica la fecha
    envio[3] = f