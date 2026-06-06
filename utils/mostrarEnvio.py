from TAD_Envio import verID, verDestinatario, verCategoria, verFecha

def mostrarEnvio(envio):
    #Muestra todos los datos de un envio
    print(f'\nID: {verID(envio)}\nDestinatario: {verDestinatario(envio)}\nCategoría del servicio: {verCategoria(envio)}\nFecha de envío: {verFecha(envio)}\n')
