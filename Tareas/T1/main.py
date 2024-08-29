from dccultivo import DCCultivo, Predio
import utils

def menu_inicio():
    while True:
        print("¡Bienvenido a DCCultivo!")
        print("*** Menú de Inicio ***")
        print("[1] Crear predios")
        print("[2] Salir del programa")
        opcion = input("Indique su opción (1, 2): ")
        if opcion in ["1", "2"]:
            return opcion
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def menu_acciones():
    print("*** Menú de Acciones ***")
    print("[1] Visualizar predio")
    print("[2] Plantar")
    print("[3] Regar")
    print("[4] Buscar y eliminar plagas")
    print("[5] Salir del programa")
    opcion = input("Indique su opción (1, 2, 3, 4, 5): ")
    return opcion

def inicia_programa():
    dccultivo = DCCultivo()
    while True:
        opcion_inicio = menu_inicio()

        if opcion_inicio == "1":
            nombre_archivo = input("Ingrese el nombre del archivo de predios: ")
            mensaje = dccultivo.crear_predios(nombre_archivo)
            print(mensaje)
            if mensaje == "Predios de DCCultivo cargados exitosamente":
                while True:
                    opcion_accion = menu_acciones()

                    if opcion_accion == "1":
                        codigo_predio = input("Ingrese el código del predio a visualizar: ")
                        predio = None
                        for i in dccultivo.predios:
                            if i.codigo_predio == codigo_predio:
                                predio = i
                                break
                        if predio:
                            utils.imprimir_planos(predio)
                        else:
                            print(f"El predio con código {codigo_predio} no existe.")

                    elif opcion_accion == "2":
                        codigo_cultivo = input("Ingrese el código del cultivo: ")
                        alto = int(input("Ingrese el alto del bloque: "))
                        ancho = int(input("Ingrese el ancho del bloque: "))
                        correcto = dccultivo.buscar_y_plantar(codigo_cultivo, alto, ancho)
                        if correcto:
                            print("Cultivo plantado exitosamente.")
                        else:
                            print("No se pudo plantar el cultivo en ningún predio.")

                    elif opcion_accion == "3":
                        codigo_predio = input("Ingrese el código del predio: ")
                        fila = int(input("Ingrese la fila de la coordenada: "))
                        columna = int(input("Ingrese la columna de la coordenada: "))
                        area = int(input("Ingrese el área de riego: "))
                        dccultivo.buscar_y_regar(codigo_predio, [fila, columna], area)
                        print("Riego aplicado exitosamente.")

                    elif opcion_accion == "4":
                        plagas_lista = utils.plagas(dccultivo)
                        resultado = dccultivo.detectar_plagas(plagas_lista)
                        print("Resultado de la eliminación de plagas:", resultado)

                    elif opcion_accion == "5":
                        print("Saliendo del programa...")
                        break
                    else:
                        print("Opción no válida. Inténtelo de nuevo.")

            else:
                continue

        elif opcion_inicio == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")


if __name__ == "__main__":
    inicia_programa()


