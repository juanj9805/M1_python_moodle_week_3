import uuid

def principal_menu_input () :
    return int(input(
        "Elige una opcion: \n"
        "1- Agregar un producto: \n"
        "2- Mostrar inventario completo: \n"
        "3- Buscar producto por nombre: \n"
        "4- Modificar producto: \n"
        "5- Eliminar producto: \n"
        "6- Mostrar estadisticas: \n"
        "7- Salir: \n"
        ))

def string_input (noun) :
    return input(f"{noun}: ")

def int_input (quantity_items) :
    return int(input(f"{quantity_items}: "))

def float_input (price_items) :
    return float(input(f"{price_items}: "))

def generate_ID () : 
    return str(uuid.uuid4())

def options () :
    return int(input(
        "Elige una opcion: \n"
        f"1- Mostrar la cantidad de productos: \n"
        f"2- Mostrar precio de todos los productos: \n"
        f"3- Mostrar producto mas caro: \n"
        f"4- Mostrar producto con mayor stock: \n"
        f"5- Salir:\n"
        ))

