import collections
from os.path import join
from utilidades import Anime  # Debes utilizar esta nametupled


#####################################
#       Parte 1 - Cargar datos      #
#####################################
def cargar_animes(ruta_archivo: str) -> list:
    anime_total = []
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos_anime = linea.strip().split(",")
            nombre = datos_anime[0]
            capitulos = int(datos_anime[1])
            puntajes = int(datos_anime[2])
            estreno = int(datos_anime[3])
            estudio = datos_anime[4]
            genero = datos_anime[5].split(";")
            anime = Anime(nombre, capitulos, puntajes, estreno, estudio, set(genero))
            anime_total.append(anime)
    return anime_total



#####################################
#        Parte 2 - Consultas        #
#####################################
def animes_por_estreno(animes: list) -> dict:
    anime_estreno = {}
    for anime in animes:
        if anime.estreno not in anime_estreno:
            anime_estreno[anime.estreno] = []
        anime_estreno[anime.estreno].append(anime.nombre)
    return anime_estreno

def descartar_animes(generos_descartados: set, animes: list) -> list:
    descartar_animes = []
    for anime in animes:
        agregar = True
        for genero in anime.generos:
            if genero in generos_descartados:
                agregar = False
                break
        if agregar:
            descartar_animes.append(anime.nombre)
    return descartar_animes


def resumen_animes_por_ver(*animes: Anime) -> dict:
    if not animes:
        return {"puntaje promedio": 0, "capitulos total": 0, "generos": set()}

    total_puntajes = 0
    total_capitulos = 0
    generos_conjuntos = set()

    for anime in animes:
        total_puntajes += anime.puntaje
        total_capitulos += anime.capitulos
        generos_conjuntos.update(anime.generos)

    puntajes_promedio = round(total_puntajes/ len(animes), 1)
    return {"puntaje promedio": puntajes_promedio, "capitulos total": total_capitulos, "generos": generos_conjuntos}


def estudios_con_genero(genero: str, **estudios: list) -> list:
    estudios_con_genero = []
    for estudio, animes in estudios.items():
        for anime in animes:
            if genero in anime.generos:
                estudios_con_genero.append(estudio)
                break
    return estudios_con_genero



if __name__ == "__main__":
    #####################################
    #       Parte 1 - Cargar datos      #
    #####################################
    animes = cargar_animes(join("data", "ejemplo.chan"))
    indice = 0
    for anime in animes:
        print(f"{indice} - {anime}")
        indice += 1

    #####################################
    #        Parte 2 - Consultas        #
    #####################################
    # Solo se usará los 2 animes del enunciado.
    datos = [
        Anime(
            nombre="Hunter x Hunter",
            capitulos=62,
            puntaje=9,
            estreno=1999,
            estudio="Nippon Animation",
            generos={"Aventura", "Comedia", "Shonen", "Acción"},
        ),
        Anime(
            nombre="Sakura Card Captor",
            capitulos=70,
            puntaje=10,
            estreno=1998,
            estudio="Madhouse",
            generos={"Shoujo", "Comedia", "Romance", "Acción"},
        ),
    ]

    # animes_por_estreno
    estrenos = animes_por_estreno(datos)
    print(estrenos)

    # descartar_animes
    animes = descartar_animes({"Comedia", "Horror"}, datos)
    print(animes)

    # resumen_animes_por_ver
    resumen = resumen_animes_por_ver(datos[0], datos[1])
    print(resumen)

    # estudios_con_genero
    estudios = estudios_con_genero(
        "Shonen",
        Nippon_Animation=[datos[0]],
        Madhouse=[datos[1]],
    )
    print(estudios)
