def confirmarAccion():
    while True:
        confirmar = input('¿Está seguro que desea realizar esta acción? (S/N): ').strip().upper()
        if(confirmar =='S'):
            return True
        elif(confirmar == 'N'):
            print('Acción cancelada.')
            return False
        else:
            print('Entrada no válida. Por favor, ingrese "S" para confirmar o "N" para cancelar.')