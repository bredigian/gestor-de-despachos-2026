def confirmarAccion(mensaje):
    while True:
        confirmar = input(f'{mensaje}\n¿Está seguro que desea realizar esta acción? (S/N): ').strip().upper()
        
        if(confirmar =='S'):
            return True

        if(confirmar == 'N'):
            print('Acción cancelada.')
            return False
        else:
            print('Entrada no válida. Por favor, ingrese "S" para confirmar o "N" para cancelar.')