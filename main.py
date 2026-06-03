from TAD_Envio import *
from TAD_Pila import *
from TAD_ListaEnvios import *
from datetime import datetime
from utils.confirmAction import confirmarAccion

from utils.datetime import obtenerFechaFinalValidada, obtenerFechaValidada, obtenerHoraValidada

categoriasServicio = ['Express', 'Estandar', 'Internacional']

def mostrarMenu():
    print('\nSeleccione una opción:')

    print('1. Alta de envíos')
    print('2. Modificación Individual')
    print('3. Eliminación Individual')
    print('4. Visualización General')
    print('5. Actualización Masiva de Prioridad')
    print('6. Generación de Pila de Despacho Prioritario')
    print('7. Depuración por Temporada')
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
        print('Ya existe un envío con el número de seguimiento proporcionado. ❌\nNo se pueden agregar envíos con IDs duplicados.')

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

    print('Envío agregado exitosamente ✅.')

def ejecutarModificacionIndividual(listaEnvios):
    print('--- Modificación Individual ---')
    
    id = input('Ingrese el número de seguimiento (Tracking ID) del envío que desea modificar: ')
    
    envio = buscarEnvioPorID(listaEnvios, id)
    if envio is None:
        print('No se encontró ningún envío con el número de seguimiento proporcionado.')

        return

    print('Se encontró el siguiente envío:')
    mostrarEnvio(envio)
    
    while True:
        mostrarMenuModificacionEnvio()

        opcion = int(input())
        match opcion:
            case 1:
                nuevoDestinatario = input('Ingrese el nuevo destinatario: ')
                if confirmarAccion(f'El destinatario se modificará de "{verDestinatario(envio)}" a "{nuevoDestinatario}".'):
                    modiDestinatario(envio, nuevoDestinatario)
                    print('Destinatario modificado exitosamente ✅.')
                
                break
            case 2:
                while True:
                    nuevaCategoriaServicio = input(f'Ingrese la nueva categoría del servicio ({", ".join(categoriasServicio)}): ')
                    if nuevaCategoriaServicio not in categoriasServicio:
                        print('Categoría de servicio no válida. Por favor, ingrese una categoría válida.')
                    else:
                        break

                if confirmarAccion(f'La categoría del servicio se modificará de "{verCategoria(envio)}" a "{nuevaCategoriaServicio}".'):
                    modiCategoria(envio, nuevaCategoriaServicio)
                    print('Categoría del servicio modificada exitosamente ✅.')
                
                break
            case 3:
                nuevaFecha = obtenerFechaValidada('Ingrese la nueva fecha de envío')
                if confirmarAccion(f'La fecha de envío se modificará de "{verFecha(envio)}" a "{nuevaFecha}".'):
                    modiFecha(envio, nuevaFecha)
                    print('Fecha de envío modificada exitosamente ✅.')

                break
            case 0:
                break
            case _:
                print('Opción no válida. Por favor, seleccione una opción válida.')

def ejecutarEliminacionIndividual(listaEnvios):
    print('--- Eliminación Individual ---')
    
    id = input('Ingrese el número de seguimiento (Tracking ID) del envío que desea eliminar: ')
    
    envio = buscarEnvioPorID(listaEnvios, id)
    if envio is None:
        print('No se encontró ningún envío con el número de seguimiento proporcionado.')

        return

    print('Se encontró el siguiente envío:')
    mostrarEnvio(envio)
    print('')
    
    if confirmarAccion(f'El envío con ID "{verID(envio)}" será eliminado.'):
        eliminarEnvio(listaEnvios, envio)
        print('Envío eliminado exitosamente ✅.')

def ejecutarActualizacionMasiva(listaEnvios):
    print('--- Actualización Masiva ---')
    
    print('Por favor, ingrese el rango de fechas para la actualización masiva.')

    fechaInicio = obtenerFechaValidada('Fecha de inicio')
    fechaFin = obtenerFechaFinalValidada(fechaInicio, 'Fecha de fin')

    nuevaHoraIngreso = obtenerHoraValidada('Ingrese la nueva hora de ingreso')

    modificacionesRealizadas = False

    for envio in listaEnvios[:]:
        fechaInicial = datetime.strptime(fechaInicio, '%d/%m/%Y %H:%M')
        fechaFinal = datetime.strptime(fechaFin, '%d/%m/%Y %H:%M')
        fechaEnvio = datetime.strptime(verFecha(envio), '%d/%m/%Y %H:%M')

        estaEnRango = fechaInicial <= fechaEnvio <= fechaFinal
        if estaEnRango:
            modificacionesRealizadas = True

            nuevaHoraIngresoDatetime = datetime.strptime(nuevaHoraIngreso, '%H:%M')
            nuevaFechaEnvio = fechaEnvio.replace(hour=nuevaHoraIngresoDatetime.hour, minute=nuevaHoraIngresoDatetime.minute)
            
            if confirmarAccion(f'La fecha de envío del envío con ID "{verID(envio)}" se modificará de "{verFecha(envio)}" a "{nuevaFechaEnvio.strftime("%d/%m/%Y %H:%M")}".'):
                modiFecha(envio, nuevaFechaEnvio.strftime('%d/%m/%Y %H:%M'))
        
    if modificacionesRealizadas:
        print('Actualización masiva completada exitosamente ✅.')
    else:
        print('No se realizaron modificaciones en el rango de fechas especificado porque no se encontraron envíos dentro del rango de fechas indicado.')

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
            if confirmarAccion(f'El envío con ID "{verID(envio)}" se eliminará.'):
                eliminarEnvio(listaEnvios, envio)
    
    print('Depuración por temporada completada exitosamente ✅.')

def generacionPilaDespachoPrioritario(listaEnvios):
    print('--- Generación de Pila de Despacho Prioritario ---')

    if listaEnviosVacia(listaEnvios):
        print('No hay envíos registrados. No se puede generar la pila de despacho prioritario.')
        return

    print('Por favor, ingrese el rango de fechas para generar la pila de despacho prioritario.')
    fechaInicio = obtenerFechaValidada('Fecha de inicio')
    fechaFin = obtenerFechaFinalValidada(fechaInicio, 'Fecha de fin')

    pilaPrioritaria = crearPila()
    
    fechaInicial = datetime.strptime(fechaInicio, '%d/%m/%Y %H:%M')
    fechaFinal = datetime.strptime(fechaFin, '%d/%m/%Y %H:%M')
    
    for envio in listaEnvios:
        fechaEnvio = datetime.strptime(verFecha(envio), '%d/%m/%Y %H:%M')
        
        estaEnRango = fechaInicial <= fechaEnvio <= fechaFinal
        if estaEnRango:
            apilar(pilaPrioritaria, envio)
    
    if pilaVacia(pilaPrioritaria):
        print('No se encontraron envíos en el rango de fechas especificado.')
        return
    
    print(f'\nSe encontraron {tamanio(pilaPrioritaria)} envíos en el rango de fechas.')
    mostrarPila(pilaPrioritaria)

def ejecutarVisualizacionEnvios(listaEnvios):
    print('--- Visualización de Envíos ---')

    if listaEnviosVacia(listaEnvios):
        print('No hay envíos registrados.')
        return
    
    enviosOrdenados = sorted(listaEnvios, key=lambda envio: datetime.strptime(verFecha(envio), '%d/%m/%Y %H:%M'))
    for envio in enviosOrdenados:
        mostrarEnvio(envio)


def ejecutarPrecargaDatos(listaEnvios):
    enviosEjemplo = [
        ['ABC123', 'Juan Pérez', 'Express', '15/04/2026 10:30'],
        ['DEF456', 'María Gómez', 'Estandar', '20/02/2026 14:45'],
        ['GHI789', 'Carlos López', 'Internacional', '25/04/2025 09:15'],
        ['JKL012', 'Ana Martínez', 'Express', '30/09/2025 16:00'],
        ['MNO345', 'Luis Rodríguez', 'Estandar', '05/10/2025 11:20'],
        ['PQR678', 'Laura Fernández', 'Express', '12/01/2026 08:00'],
        ['STU901', 'Ayrton Silva', 'Internacional', '18/03/2026 13:30'],
        ['VWX234', 'Sofía Torres', 'Estandar', '22/05/2026 15:45'],
        ['YZA567', 'Diego Ramírez', 'Express', '07/06/2025 09:00'],
        ['BCD890', 'Ariana Sampedro', 'Internacional', '14/08/2025 17:20'],
        ['EFG123', 'Roberto García', 'Estandar', '28/11/2025 12:10'],
        ['HIJ456', 'Patricia Morales', 'Express', '03/12/2025 10:45'],
        ['KLM789', 'Fernando Castro', 'Internacional', '19/01/2026 16:30'],
        ['NOP012', 'Elena Vargas', 'Estandar', '25/03/2026 11:15'],
        ['QRS345', 'Gianluca Bredice', 'Express', '08/04/2026 14:00'],
        ['TUV678', 'Isabel Jiménez', 'Internacional', '17/05/2026 09:30'],
        ['WXY901', 'Andrés Medina', 'Estandar', '21/07/2025 13:50'],
        ['ZAB234', 'Gabriela Ortiz', 'Express', '29/08/2025 08:25'],
        ['CDE567', 'Ricardo Navarro', 'Internacional', '10/10/2025 15:40'],
        ['FGH890', 'Valentina Cruz', 'Estandar', '16/02/2026 12:00'],
    ]

    for envioData in enviosEjemplo:
        envio = crearEnvio()
        cargarEnvio(envio, verID(envioData), verDestinatario(envioData), verCategoria(envioData), verFecha(envioData))
        agregarEnvio(listaEnvios, envio)

def main():
    print('--- Sistema de Gestión de Despachos ---')
    
    listaEnvios = crearListaEnvios()

    ejecutarPrecargaDatos(listaEnvios)

    while True:
        mostrarMenu()
        
        opcion = int(input())
        match opcion:
            case 1:
                ejecutarAltaEnvio(listaEnvios)
            case 2:
                ejecutarModificacionIndividual(listaEnvios)
            case 3:
                ejecutarEliminacionIndividual(listaEnvios)
            case 4:
                ejecutarVisualizacionEnvios(listaEnvios)
            case 5:
                ejecutarActualizacionMasiva(listaEnvios)
            case 6:
                generacionPilaDespachoPrioritario(listaEnvios)
            case 7:
                ejecutarDepuracionPorTemporada(listaEnvios)
            case 0:
                print('Saliendo del programa...')
                break
            case _:
                print('Opción no válida. Por favor, seleccione una opción válida.')

main()