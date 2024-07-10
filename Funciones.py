import random as rd
import csv

def asignar_sueldos(trabajadores_lista):
    
    sueldo_trabajadores_dicc = {}
    sueldo_trabajadores_dicc = {elemento : 0 for elemento in trabajadores_lista}
    for elemento in trabajadores_lista:
        sueldo_aleatorio = rd.randint(300000, 2500000)
        sueldo_trabajadores_dicc[elemento] = sueldo_aleatorio
    print(sueldo_trabajadores_dicc)
    print("Sueldos Asignados Correctamente\n")    

    return sueldo_trabajadores_dicc

def clasificacion_sueldos(trabajadores_lista_sueldo):
    sueldos_min = {}
    sueldos_mid = {}
    sueldos_max = {}
    for keys,values in trabajadores_lista_sueldo.items():
        if values < 800000:
            sueldos_min[keys] = values
        elif values >= 800000 and values <= 2000000:
            sueldos_mid[keys] = values
        elif values > 2000000:
            sueldos_max[keys] = values
    sueldos_min_lista = list(sueldos_min.values())
    sueldos_mid_lista = list(sueldos_mid.values())
    sueldos_max_lista = list(sueldos_max.values())
    print("Sueldos menores a $800.000 TOTAL: ", len(sueldos_min_lista))
    print("Nombre Empleado\t\t Sueldo")
    for keys,values in sueldos_min.items():
        print(keys,"\t\t", values)
    print("")
    print("Sueldos entre $800.000 y $2.000.000\nTOTAL: ", len(sueldos_mid_lista))
    print("Nombre Empleado\t\t Sueldo")
    for keys,values in sueldos_mid.items():
        print(keys,"\t\t", values)
    print("")
    print("Sueldos superiores a $2.000.000\nTOTAL: ", len(sueldos_max_lista))
    print("Nombre Empleado\t\t Sueldo")
    for keys,values in sueldos_max.items():
        print(keys,"\t\t", values)
    print()    
    
    return sueldos_min_lista,sueldos_mid_lista,sueldos_max_lista

def estadisticas_sueldos(trabajadores_lista_sueldos,sueldos_min_lista,sueldos_mid_lista,sueldos_max_lista):
    print("El sueldo mas bajo es: $", min(sueldos_min_lista))
    print("El sueldo mas alto es: $", max(sueldos_mid_lista))
    lista_sueldos_completa = list(trabajadores_lista_sueldos.values())
    print("El promedio de los sueldos es: $", sum(lista_sueldos_completa) / len(lista_sueldos_completa))

def exportacion_sueldos(trabajadores_lista_sueldos):
    sueldo_detalle = {}

    for keys,values in trabajadores_lista_sueldos.items():
        sueldo_detalle[keys] = {"Sueldo Base": values, "Descuento Salud": round(values * 0.07), "DescuentoAFP": round(values * 0.12), "Sueldo Liquido": round(values - (values * 0.07) - (values *0.12))}

    print("Nombre de Empleado\tSueldo Base\tDescuento Salud\tDescuento AFP\tSueldo Liquido")
    for keys,values in sueldo_detalle.items():
        print(f"{keys}\t\t{values["Sueldo Base"]}\t\t{values["Descuento Salud"]}\t\t{values["DescuentoAFP"]}\t\t{values["Sueldo Liquido"]}")    
    with open("planilla_sueldos.csv","w") as archivo:
        encabezado = ["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo liquido"]
        escritor = csv.writer(archivo,delimiter=",")
        escritor.writerow(encabezado)

        for keys,values in sueldo_detalle.items():
            nombre = sueldo_detalle[values["Nombre empleado"]]
            sueldo = sueldo_detalle[values["Sueldo Base"]]
            descsal = sueldo_detalle[values["Descuento Salud"]]
            desafp = sueldo_detalle[values["DescuentoAFP"]]
            liquido = sueldo_detalle[values["Sueldo Liquido"]]
            escritor.writerow(nombre,sueldo,descsal,desafp,liquido)