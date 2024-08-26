import os
class Predio:
    def __init__(self, codigo_predio: str, alto: int, ancho: int) -> None:
        self.codigo_predio = codigo_predio
        self.alto = alto
        self.ancho = ancho
        self.plano = []
        self.plano_riego = []

    def crear_plano(self, tipo: str) -> None:
        plano = []

        for i in range(self.alto):
            fila = []

            for j in range(self.ancho):
                if tipo == "normal":
                    fila.append("X")
                elif tipo == "riego":
                    fila.append(0)

            plano.append(fila)
        if tipo == "normal":
            self.plano = plano
        elif tipo == "riego":
            self.plano_riego = plano

    def plantar(self, codigo_cultivo: int, coordenadas: list, alto: int, ancho: int) -> None:
        fila_inicio, columna_inicio = coordenadas

        for i in range(alto):
            for j in range(ancho):
                self.plano[fila_inicio+i][columna_inicio+j] = codigo_cultivo

    def regar(self, coordenadas: list, area: int) -> None:
        fila_centro, columna_centro = coordenadas

        radio = area
        lado = 2 * radio

        fila_min = fila_centro - radio
        fila_max = fila_centro + radio
        columna_min = columna_centro - radio
        columna_max = columna_centro + radio

        # Crear un conjunto de coordenadas para las esquinas
        esquinas = {
            (fila_min, columna_min),
            (fila_min, columna_max),
            (fila_max, columna_min),
            (fila_max, columna_max)
        }

        # Iterar sobre cada celda en el plano de riego
        for i in range(self.alto):
            for j in range(self.ancho):
                # Verificar si la celda está dentro del área del cuadrado
                if fila_min <= i <= fila_max and columna_min <= j <= columna_max:
                    # Verificar si la celda no está en las esquinas
                    if (i, j) not in esquinas:
                        self.plano_riego[i][j] += 1


    def eliminar_cultivo(self, codigo_cultivo: int) -> int:
        celda_eliminado = 0

        for i in range(self.alto):
            for j in range(self.ancho):
                if self.plano[i][j] == codigo_cultivo:
                    self.plano[i][j] = "X"
                    celda_eliminado += 1

        return celda_eliminado


class DCCultivo:
    def __init__(self) -> None:
        self.predios = []

    def crear_predios(self, nombre_archivo: str) -> str:
        # Verificar si el archivo existe
        if not os.path.exists("data\\"+nombre_archivo):
            return "Fallo en la carga de DCCultivo"


        with open("data\\"+nombre_archivo, "r") as archivo:

            lineas = archivo.readlines()
            if not lineas:
                return "Fallo en la carga de DCCultivo"

            self.predios = []

            for linea in lineas:
                codigo, alto, ancho = linea.strip().split(",")
                predio = Predio(codigo, int(alto), int(ancho))
                predio.crear_plano("normal")
                predio.crear_plano("riego")
                self.predios.append(predio)

        return "Predios de DCCultivo cargados exitosamente"

    def buscar_y_plantar(self, codigo_cultivo: int, alto: int, ancho: int) -> bool:
        for predio in self.predios:
            for fila in range(predio.alto - alto +1):
                for columna in range(predio.ancho - ancho +1):
                    espace_suficiente = True

                    for i in range(alto):
                        for j in range(ancho):
                            if predio.plano[fila + i][columna + j] != "X":
                                espace_suficiente = False
                                break
                            if not espace_suficiente:
                                break

                    if espace_suficiente:
                        predio.plantar(codigo_cultivo, [fila, columna], alto, ancho)
                        return True

        return False


    def buscar_y_regar(self, codigo_predio: str, coordenadas: list, area: int) -> None:
        for predio in self.predios:
            if predio.codigo_predio == codigo_predio:
                predio.regar(coordenadas, area)
                break

    def detectar_plagas(self, lista_plagas: list[list]) -> list[list]:
        afectados = []

        for codigo, coordenadas in lista_plagas:
            for predio in self.predios:
                if predio.codigo_predio == codigo:
                    celdas_eliminadas = predio.eliminar_cultivo(coordenadas)
                    if celdas_eliminadas > 0:
                        afectados.append([codigo, celdas_eliminadas])
                    break

        afectados.sort(key=lambda x: (x[1], x[0]))

        return afectados

