# TAD Envio
# envio = [trackingID, destinatario, categoria, fecha, hora]
#           [0]          [1]           [2]        [3]    [4]

def crearEnvio(id, destinatario, categoria, fecha):
    #Crea un envio vacio
    envio = [id, destinatario, categoria, fecha]
    
    return envio

def cargarEnvio(envio, id, destinatario, categoria, fecha, hora):
    #Carga los datos de un envio
    envio[0] = id
    envio[1] = destinatario
    envio[2] = categoria
    envio[3] = fecha
    envio[4] = hora

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

def verHora(envio):
    #Retorna la hora
    return envio[4]

def modiDestinatario(envio, d):
    #Modifica el destinatario
    envio[1] = d

def modiCategoria(envio, c):
    #Modifica la categoria
    envio[2] = c

def modiFecha(envio, f):
    #Modifica la fecha
    envio[3] = f

def modiHora(envio, h):
    #Modifica la hora
    envio[4] = h

def mostrarEnvio(envio):
    #Muestra todos los datos de un envio
    print("  ID:          ", verID(envio))
    print("  Destinatario:", verDestinatario(envio))
    print("  Categoria:   ", verCategoria(envio))
    print("  Fecha:       ", verFecha(envio))
    print("  Hora:        ", verHora(envio))
