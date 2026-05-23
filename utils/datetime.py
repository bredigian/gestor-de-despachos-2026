from datetime import datetime

def obtenerFechaValidada(mensaje, excluirHora=False):
    while True:
        try:
            fecha = input(f'{mensaje} {"(DD/MM/AAAA)" if excluirHora else "(DD/MM/AAAA HH:MM)"}: ')
            datetime.strptime(fecha, '%d/%m/%Y' if excluirHora else '%d/%m/%Y %H:%M')

            break
        except ValueError:
            print(f'Formato de fecha no válido. Por favor, ingrese la fecha en el formato {"DD/MM/AAAA" if excluirHora else "DD/MM/AAAA HH:MM"}.')
    
    return fecha

def obtenerFechaFinalValidada(fechaInicio, mensaje, excluirHora=False):
    while True:
        try:
            fecha = input(f'{mensaje} {"(DD/MM/AAAA)" if excluirHora else "(DD/MM/AAAA HH:MM)"}: ')
            fechaFinalFormateada = datetime.strptime(fecha, '%d/%m/%Y' if excluirHora else '%d/%m/%Y %H:%M')
            fechaInicioFormateada = datetime.strptime(fechaInicio, '%d/%m/%Y' if excluirHora else '%d/%m/%Y %H:%M')

            if fechaFinalFormateada >= fechaInicioFormateada:
                break
            else:
                print('La fecha final no puede ser anterior a la fecha de inicio. Por favor, ingrese una fecha válida.')
        except ValueError:
            print(f'Formato de fecha no válido. Por favor, ingrese la fecha en el formato {"DD/MM/AAAA" if excluirHora else "DD/MM/AAAA HH:MM"}.')

    return fecha

def obtenerHoraValidada(mensaje):
    while True:
        try:
            hora = input(f'{mensaje} (HH:MM): ')
            datetime.strptime(hora, '%H:%M')

            break
        except ValueError:
            print('Formato de hora no válido. Por favor, ingrese la hora en el formato HH:MM.')
    
    return hora