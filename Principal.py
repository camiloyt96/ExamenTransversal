import csv
import Funciones as fn
trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]
trabajadores_creditos = {}
while True:
    try:
        print("1) Asignar sueldos Aleatorios")
        print("2) Clasificar sueldos")
        print("3) Ver estadisticas")
        print("4) Reporte de sueldos")
        print("5) Salir del programa")

        opc = int(input("Ingrese opcion\n"))

        if opc == 1:
            trabajadores_creditos = fn.asignar_sueldos(trabajadores)
        elif opc == 2:
            if not trabajadores_creditos:
                print("Debe asignar creditos primero, vuelva a intentarlo porfavor")
            else:
                sueldos_min_lista,sueldos_mid_lista,sueldos_max_lista = fn.clasificacion_sueldos(trabajadores_creditos)
        elif opc == 3:
            if not trabajadores_creditos:
                print("Debe asignar creditos primero, vuelva a intentarlo porfavor")
            else:
                fn.estadisticas_sueldos(trabajadores_creditos,sueldos_min_lista,sueldos_mid_lista,sueldos_max_lista)
        elif opc == 4:
            if not trabajadores_creditos:
                print("Debe asignar creditos primero, vuelva a intentarlo porfavor")
            else:
                descuento_salud,descuento_afp,sueldo_liquido = fn.exportacion_sueldos(trabajadores_creditos)
        elif opc == 5:
            print("Finalizando programa...")
            print("Desarrollado por Camilo Yanez Troncoso")
            print("RUT 20.215.309-7")
            break
        else:
            print("La opcion elegida tiene que ser un numero entre 1 y 5, vuelva a intentarlo porfavor. ")
    except:
        print("La opcion elegida tiene que ser un numero entre 1 y 5, vuelva a intentarlo porfavor.")