from TAD_Envio import *
from TAD_Pila import *
from TAD_ListaEnvios import *
from datetime import datetime

categoriasServicio = ['Express', 'Estandar', 'Internacional']

def mostrarMenu():
    print('Seleccione una opción:')

    print('1. Alta de envíos')
    print('2. Modificación y Eliminación Individual')
    print('0. Salir')

def ejecutarAltaEnvio(listaEnvios):
    print('--- Alta de Envíos ---')

    id = input('Ingrese el número de seguimiento (Tracking ID): ')
    destinatario = input('Ingrese el destinatario: ')

    while True:
        categoriaServicio = input(f'Ingrese la categoría del servicio ({", ".join(categoriasServicio)}): ') # "toma este string (coma-espacio) y úsalo para unir los elementos de la lista"
        if categoriaServicio not in categoriasServicio:
            print('Categoría de servicio no válida. Por favor, ingrese una categoría válida.')
        else:
            break

    while True:
        try:
            fecha = input('Ingrese la fecha de envío (DD/MM/AAAA HH:MM): ')
            datetime.strptime(fecha, '%d/%m/%Y %H:%M')
            break
        except ValueError:
            print('Formato de fecha no válido. Por favor, ingrese la fecha en el formato DD/MM/AAAA HH:MM.')
    
    envio = crearEnvio(id, destinatario, categoriaServicio, fecha)
    agregarEnvio(listaEnvios, envio)

    print('Envío agregado exitosamente.')

def ejecutarModificacionEliminacionIndividual():
    print('--- Modificación y Eliminación Individual ---')
    print('Esta funcionalidad aún no está disponible.')

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
                ejecutarModificacionEliminacionIndividual()
            case 0:
                print('Saliendo del programa...')
                break
            case _:
                print('Opción no válida. Por favor, seleccione una opción válida.')


main()