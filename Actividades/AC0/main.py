from entities import Item, Usuario
from utils.pretty_print import print_usuario, print_canasta, print_items

def cargar_items() -> list:
    items = []
    with open("utils/items.dcc", "r") as archivo:
        for linea in archivo:
            nombre, precio, puntos = linea.strip().split(",")
            item = Item(nombre, int(precio), int(puntos))
            items.append(item)
    return items

def crear_usuario(tiene_suscripcion: bool) -> Usuario:
    usuario = Usuario(tiene_suscripcion)
    print_usuario(usuario)
    return usuario


if __name__ == "__main__":
     # 1) Crear usuario (puede ser con o sin suscripcion)
     usuario = crear_usuario(True)

     # 2) Cargar los items
     items = cargar_items()

     # 3) Imprimir todos los items usando los módulos de pretty_print
     print_items = print_items(items)

     # 4) Agregar todos los items a la canasta del usuario
     for item in items:
         usuario.agregar_item(item)

     # 5) Imprimir la canasta del usuario usando los módulos de pretty_print
     print_canasta(usuario)

     # 6) Generar la compra desde el usuario
     usuario.comprar()

     # 7) Imprimir el usuario usando los módulos de pretty_print
     print_usuario(usuario)


