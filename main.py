from TAD_Envio import *
from TAD_Pila import *
from TAD_ListaEnvios import *
from datetime import datetime
from utils.confirmAction import confirmarAccion

from utils.datetime import obtenerFechaValidada, obtenerHoraValidada

categoriasServicio = ['Express', 'Estandar', 'Internacional']

def mostrarMenu():
    print('\nSeleccione una opción:')

    print('1. Alta de envíos')
    print('2. Modificación y Eliminación Individual')
    print('3. Visualización General')
    print('4. Actualización Masiva de Prioridad')
    print('6. Depuración por Temporada')
    print('0. Salir')

def mostrarMenuModificacionEnvio():
    print('Seleccione el tipo de modificación:')

    print('1. Modificar destinatario')
    print('2. Modificar categoría del servicio')
    print('3. Modificar fecha de envío')
    print('4. Eliminar envío')
    print('0. Volver al menú principal')

def ejecutarAltaEnvio(listaEnvios):
    print('--- Alta de Envíos ---')

    id = input('Ingrese el número de seguimiento (Tracking ID): ')
    envioExistente = buscarEnvioPorID(listaEnvios, id)
    if envioExistente is not None:
        print('Ya existe un envío con el número de seguimiento proporcionado. No se pueden agregar envíos con IDs duplicados.')

        return
    
    destinatario = input('Ingrese el destinatario: ')

    while True:
        categoriaServicio = input(f'Ingrese la categoría del servicio ({", ".join(categoriasServicio)}): ') # "toma este string (coma-espacio) y úsalo para unir los elementos de la lista"
        if categoriaServicio not in categoriasServicio:
            print('Categoría de servicio no válida. Por favor, ingrese una categoría válida.')
        else:
            break

    fecha = obtenerFechaValidada('Ingrese la fecha de envío')
    
    envio = crearEnvio()
    cargarEnvio(envio, id, destinatario, categoriaServicio, fecha)
    agregarEnvio(listaEnvios, envio)

    print('Envío agregado exitosamente.')

def ejecutarModificacionEliminacionIndividual(listaEnvios):
    print('--- Modificación y Eliminación Individual ---')
    
    id = input('Ingrese el número de seguimiento (Tracking ID) del envío que desea modificar: ')
    
    envio = buscarEnvioPorID(listaEnvios, id)
    if envio is None:
        print('No se encontró ningún envío con el número de seguimiento proporcionado.')

        return
    
    while True:
        mostrarMenuModificacionEnvio()

        opcion = int(input())
        match opcion:
            case 1:
                nuevoDestinatario = input('Ingrese el nuevo destinatario: ')
                if confirmarAccion():
                    modiDestinatario(envio, nuevoDestinatario)
                    print('Destinatario modificado exitosamente.')
                
                break
            case 2:
                while True:
                    nuevaCategoriaServicio = input(f'Ingrese la nueva categoría del servicio ({", ".join(categoriasServicio)}): ')
                    if nuevaCategoriaServicio not in categoriasServicio:
                        print('Categoría de servicio no válida. Por favor, ingrese una categoría válida.')
                    else:
                        break

                if confirmarAccion():
                    modiCategoria(envio, nuevaCategoriaServicio)
                    print('Categoría del servicio modificada exitosamente.')
                
                break
            case 3:
                nuevaFecha = obtenerFechaValidada('Ingrese la nueva fecha de envío')
                if confirmarAccion():
                    modiFecha(envio, nuevaFecha)
                    print('Fecha de envío modificada exitosamente.')

                break
            case 4:
                if confirmarAccion():
                    eliminarEnvio(listaEnvios, envio)
                    print('Envío eliminado exitosamente.')

                break
            case 0:
                break
            case _:
                print('Opción no válida. Por favor, seleccione una opción válida.')

def ejecutarActualizacionMasiva(listaEnvios):
    print('--- Actualización Masiva ---')
    
    print('Por favor, ingrese el rango de fechas para la actualización masiva.')

    fechaInicio = obtenerFechaValidada('Fecha de inicio', True)
    fechaFin = obtenerFechaValidada('Fecha de fin', True)

    nuevaHoraIngreso = obtenerHoraValidada('Ingrese la nueva hora de ingreso')

    for envio in listaEnvios[:]:
        fechaInicial = datetime.strptime(fechaInicio, '%d/%m/%Y')
        fechaFinal = datetime.strptime(fechaFin, '%d/%m/%Y')
        fechaEnvio = datetime.strptime(verFecha(envio), '%d/%m/%Y %H:%M')

        estaEnRango = fechaInicial <= fechaEnvio <= fechaFinal
        if estaEnRango:
            nuevaFechaEnvio = fechaEnvio.replace(hour=datetime.strptime(nuevaHoraIngreso, '%H:%M').hour, minute=datetime.strptime(nuevaHoraIngreso, '%H:%M').minute)
            modiFecha(envio, nuevaFechaEnvio.strftime('%d/%m/%Y %H:%M'))
        
    print('Actualización masiva completada exitosamente.')

def ejecutarDepuracionPorTemporada(listaEnvios):
    print('--- Depuración por Temporada ---')

    if listaEnviosVacia(listaEnvios):
        print('No hay envíos registrados. No se puede realizar la depuración por temporada.')

        return
    
    print('Por favor, ingrese el mes que desea depurar (1-12): ')

    while True:
        try:
            mesDepuracion = int(input())
            if 1 <= mesDepuracion <= 12:
                break
            else:
                print('Mes no válido. Por favor, ingrese un número entre 1 y 12.')
        except ValueError:
            print('Entrada no válida. Por favor, ingrese un número entre 1 y 12.')
    
    for envio in listaEnvios[:]:
        fechaEnvio = datetime.strptime(verFecha(envio), '%d/%m/%Y %H:%M')
        if fechaEnvio.month == mesDepuracion:
            eliminarEnvio(listaEnvios, envio)
    
    print('Depuración por temporada completada exitosamente.')

def ejecutarVisualizacionEnvios(listaEnvios):
    print('--- Visualización de Envíos ---')

    if listaEnviosVacia(listaEnvios):
        print('No hay envíos registrados.')
        return
    
    enviosOrdenados = sorted(listaEnvios, key=lambda envio: datetime.strptime(verFecha(envio), '%d/%m/%Y %H:%M'))
    for envio in enviosOrdenados:
        mostrarEnvio(envio)
def main():
    print('--- Sistema de Gestión de Despachos ---')
    
    listaEnvios = crearListaEnvios()

    while True:
        mostrarMenu()
        
        opcion = int(input())
        match opcion:
            case 1:
                ejecutarAltaEnvio(listaEnvios)
            case 2:
                ejecutarModificacionEliminacionIndividual(listaEnvios)
            case 3:
                ejecutarVisualizacionEnvios(listaEnvios)
            case 4:
                ejecutarActualizacionMasiva(listaEnvios)
            case 6:
                ejecutarDepuracionPorTemporada(listaEnvios)
            case 0:
                print('Saliendo del programa...')
                break
            case _:
                print('Opción no válida. Por favor, seleccione una opción válida.')


main()