from TAD_Envio import *
from TAD_Pila import *
from TAD_ListaEnvios import *
from datetime import datetime
from utils.confirmAction import confirmarAccion

from utils.datetime import obtenerFechaFinalValidada, obtenerFechaValidada, obtenerHoraValidada

categoriasServicio = ['EXPRESS', 'ESTANDAR', 'INTERNACIONAL']

def mostrarMenu():
    print('\nEstas son las opciones disponibles. Por favor, seleccione una opción para continuar:')

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
        if categoriaServicio.upper() not in categoriasServicio:
            print('Categoría de servicio no válida. Por favor, ingrese una categoría válida.')
        else:
            break

    fecha = obtenerFechaValidada('Ingrese la fecha de envío')
    
    envio = crearEnvio()
    cargarEnvio(envio, id, destinatario, categoriaServicio, fecha)
    agregarEnvio(listaEnvios, envio)

    print('\nEl siguiente envío fue agregado exitosamente ✅:')
    mostrarEnvio(envio)

    input('Presione Enter para continuar...')

def ejecutarModificacionIndividual(listaEnvios):
    print('--- Modificación Individual ---')
    
    id = input('Ingrese el número de seguimiento (Tracking ID) del envío que desea modificar: ')
    
    envio = buscarEnvioPorID(listaEnvios, id)
    if envio is None:
        print('No se encontró ningún envío con el número de seguimiento proporcionado.')

        return

    print('Se encontró el siguiente envío:')
    mostrarEnvio(envio)

    envioModificado = False
    
    while True:
        mostrarMenuModificacionEnvio()

        opcion = input()
        match opcion:
            case '1':
                nuevoDestinatario = input('Ingrese el nuevo destinatario: ')
                if confirmarAccion(f'El destinatario se modificará de "{verDestinatario(envio)}" a "{nuevoDestinatario}".'):
                    modiDestinatario(envio, nuevoDestinatario)
                    print('\nDestinatario modificado exitosamente ✅.')

                    envioModificado = True

                break
            case '2':
                while True:
                    nuevaCategoriaServicio = input(f'Ingrese la nueva categoría del servicio ({", ".join(categoriasServicio)}): ')
                    nuevaCategoriaServicioMayuscula = nuevaCategoriaServicio.upper()
                    
                    if nuevaCategoriaServicioMayuscula not in categoriasServicio:
                        print('Categoría de servicio no válida. Por favor, ingrese una categoría válida.')
                    else:
                        break

                if confirmarAccion(f'La categoría del servicio se modificará de "{verCategoria(envio)}" a "{nuevaCategoriaServicioMayuscula}".'):
                    modiCategoria(envio, nuevaCategoriaServicioMayuscula)
                    print('\nCategoría del servicio modificada exitosamente ✅.')

                    envioModificado = True
                
                break
            case '3':
                nuevaFecha = obtenerFechaValidada('Ingrese la nueva fecha de envío')
                if confirmarAccion(f'La fecha de envío se modificará de "{verFecha(envio)}" a "{nuevaFecha}".'):
                    modiFecha(envio, nuevaFecha)
                    print('\nFecha de envío modificada exitosamente ✅.')

                    envioModificado = True

                break
            case '0':
                break
            case _:
                print('Opción no válida. Por favor, seleccione una opción válida.')
    
    if envioModificado:
        print('El envío quedó modificado de la siguiente manera:')
        mostrarEnvio(envio)

    input('Presione Enter para continuar...')


def ejecutarEliminacionIndividual(listaEnvios):
    print('--- Eliminación Individual ---')
    
    id = input('Ingrese el número de seguimiento (Tracking ID) del envío que desea eliminar: ')
    
    envio = buscarEnvioPorID(listaEnvios, id)
    if envio is None:
        print('No se encontró ningún envío con el número de seguimiento proporcionado.')

        return

    print('Se encontró el siguiente envío:')
    mostrarEnvio(envio)
    
    if confirmarAccion('El envío será eliminado.'):
        eliminarEnvio(listaEnvios, envio)
        print('Envío eliminado exitosamente ✅.')
    
    input('Presione Enter para continuar...')

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
    
    input('Presione Enter para continuar...')

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
    input('Presione Enter para continuar...')

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

    input('Presione Enter para continuar...')

def ejecutarVisualizacionEnvios(listaEnvios):
    print('--- Visualización de Envíos ---')

    if listaEnviosVacia(listaEnvios):
        print('No hay envíos registrados.')
        return
    
    for envio in listaEnvios:
        mostrarEnvio(envio)

    input('Presione Enter para continuar...')

def ejecutarPrecargaDatos(listaEnvios):
    enviosEjemplo = [
        ['ABC123', 'Juan Pérez', 'EXPRESS', '15/04/2026 10:30'],
        ['DEF456', 'María Gómez', 'ESTANDAR', '20/02/2026 14:45'],
        ['GHI789', 'Carlos López', 'INTERNACIONAL', '25/04/2025 09:15'],
        ['JKL012', 'Ana Martínez', 'EXPRESS', '30/09/2025 16:00'],
        ['MNO345', 'Luis Rodríguez', 'ESTANDAR', '05/10/2025 11:20'],
        ['PQR678', 'Laura Fernández', 'EXPRESS', '12/01/2026 08:00'],
        ['STU901', 'Ayrton Silva', 'INTERNACIONAL', '18/03/2026 13:30'],
        ['VWX234', 'Sofía Torres', 'ESTANDAR', '22/05/2026 15:45'],
        ['YZA567', 'Diego Ramírez', 'EXPRESS', '07/06/2025 09:00'],
        ['BCD890', 'Ariana Sampedro', 'INTERNACIONAL', '14/08/2025 17:20'],
        ['EFG123', 'Roberto García', 'ESTANDAR', '28/11/2025 12:10'],
        ['HIJ456', 'Patricia Morales', 'EXPRESS', '03/12/2025 10:45'],
        ['KLM789', 'Fernando Castro', 'INTERNACIONAL', '19/01/2026 16:30'],
        ['NOP012', 'Elena Vargas', 'ESTANDAR', '25/03/2026 11:15'],
        ['QRS345', 'Gianluca Bredice', 'EXPRESS', '08/04/2026 14:00'],
        ['TUV678', 'Isabel Jiménez', 'INTERNACIONAL', '17/05/2026 09:30'],
        ['WXY901', 'Andrés Medina', 'ESTANDAR', '21/07/2025 13:50'],
        ['ZAB234', 'Gabriela Ortiz', 'EXPRESS', '29/08/2025 08:25'],
        ['CDE567', 'Ricardo Navarro', 'INTERNACIONAL', '10/10/2025 15:40'],
        ['FGH890', 'Valentina Cruz', 'ESTANDAR', '16/02/2026 12:00'],
        ['LMN135', 'Tomás Herrera', 'EXPRESS', '02/05/2026 09:45'],
        ['OPQ246', 'Camila Rojas', 'ESTANDAR', '11/06/2026 14:20'],
        ['RST357', 'Martín Suárez', 'INTERNACIONAL', '27/07/2025 10:10'],
        ['UVW468', 'Julieta Acosta', 'EXPRESS', '05/08/2025 16:35'],
        ['XYZ579', 'Nicolás Benítez', 'ESTANDAR', '13/09/2025 11:50'],
        ['ACE680', 'Florencia Duarte', 'INTERNACIONAL', '24/10/2025 08:40'],
        ['BDF791', 'Matías Cabrera', 'EXPRESS', '06/11/2025 15:25'],
        ['CEG802', 'Milagros Ponce', 'ESTANDAR', '18/12/2025 12:55'],
        ['DFH913', 'Joaquín Molina', 'INTERNACIONAL', '09/01/2026 17:10'],
        ['EGI024', 'Agustina Vega', 'EXPRESS', '22/02/2026 10:20'],
        ['FHJ135', 'Bruno Peralta', 'ESTANDAR', '04/03/2026 13:15'],
        ['GIK246', 'Lucía Salazar', 'INTERNACIONAL', '15/04/2026 18:05'],
        ['HJL357', 'Federico Luna', 'EXPRESS', '28/05/2026 09:35'],
        ['IKM468', 'Victoria Campos', 'ESTANDAR', '10/06/2025 14:50'],
        ['JLN579', 'Santiago Núñez', 'INTERNACIONAL', '21/07/2025 11:05'],
        ['KMO680', 'Carolina Ferreyra', 'EXPRESS', '03/08/2025 16:15'],
        ['LNP791', 'Emiliano Quiroga', 'ESTANDAR', '14/09/2025 08:55'],
        ['MOQ802', 'Daniela Aguirre', 'INTERNACIONAL', '26/10/2025 13:40'],
        ['NPR913', 'Gonzalo Villalba', 'EXPRESS', '07/12/2025 15:30'],
        ['OQS024', 'Natalia Figueroa', 'ESTANDAR', '19/01/2026 10:05']

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
        
        opcion = input()
        match opcion:
            case '1':
                ejecutarAltaEnvio(listaEnvios)
            case '2':
                ejecutarModificacionIndividual(listaEnvios)
            case '3':
                ejecutarEliminacionIndividual(listaEnvios)
            case '4':
                ejecutarVisualizacionEnvios(listaEnvios)
            case '5':
                ejecutarActualizacionMasiva(listaEnvios)
            case '6':
                generacionPilaDespachoPrioritario(listaEnvios)
            case '7':
                ejecutarDepuracionPorTemporada(listaEnvios)
            case '0':
                print('Saliendo del programa...')
                break
            case _:
                print('Opción no válida. Por favor, seleccione una opción válida.')

main()